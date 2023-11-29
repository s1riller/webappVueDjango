from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils import timezone
from django.utils.crypto import get_random_string
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

from django.conf import settings
from .managers import UserManager
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email'), unique=True)
    first_name = models.CharField(_('name'), max_length=30, blank=True)
    last_name = models.CharField(_('surname'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('registered'), auto_now_add=True)
    is_active = models.BooleanField(_('is_active'), default=False)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    confirmation_token = models.CharField(_('confirmation_token'), max_length=30, blank=True)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('Пользователь')
        verbose_name_plural = _('Пользователи')

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def generate_confirmation_token(self):
        token = get_random_string(length=30)
        self.confirmation_token = token
        self.save()
        return token


from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование')
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='children',
                               verbose_name='Родительская категория')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


from django.db import models
from django.contrib.auth.models import User  # Импортируйте модель пользователя, которую вы используете в проекте


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    stock_quantity = models.PositiveIntegerField(default=0, verbose_name='Количество на складе')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')

    # Поля, специфичные для категории "Лекарства"
    is_prescription_required = models.BooleanField(default=False, verbose_name='Требуется рецепт')

    # Поля, специфичные для категории "Одежда"
    size = models.CharField(max_length=20, blank=True, null=True, verbose_name='Размер')
    color = models.CharField(max_length=50, blank=True, null=True, verbose_name='Цвет')

    # Поля, специфичные для категории "Электроника"
    brand = models.CharField(max_length=100, blank=True, null=True, verbose_name='Бренд')
    model = models.CharField(max_length=100, blank=True, null=True, verbose_name='Модель')

    # Другие общие поля
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    # Поля для мусорной корзины
    is_deleted = models.BooleanField(default=False, verbose_name='Удален')
    deleted_at = models.DateTimeField(null=True, blank=True, verbose_name='Дата удаления')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name

    def soft_delete(self):
        """
        Помечает товар как удаленный и перемещает его в мусорную корзину.
        """
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

        # Создаем запись в мусорной корзине
        TrashBin.objects.create(product=self)

    def restore(self):
        """
        Восстанавливает товар из мусорной корзины.
        """
        self.is_deleted = False
        self.deleted_at = None
        self.save()

        # Удаляем запись из мусорной корзины
        TrashBin.objects.filter(product=self).delete()


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images', verbose_name='Продукт')
    image = models.ImageField(upload_to='product_images/', verbose_name='Изображение')

    class Meta:
        verbose_name = 'Изображение продукта'
        verbose_name_plural = 'Изображения продуктов'

    def __str__(self):
        return f'{self.product.name} - Image {self.pk}'


class TrashBin(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, primary_key=True,
                                   verbose_name='Продукт в корзине')
    deleted_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата удаления')

    class Meta:
        verbose_name = 'Мусорная корзина'
        verbose_name_plural = 'Мусорная корзины'

    def __str__(self):
        return f'TrashBin for {self.product.name}'


class ActivityLog(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, blank=True,
                             verbose_name='Пользователь')
    action = models.CharField(max_length=255, verbose_name='Действие')
    timestamp = models.DateTimeField(default=timezone.now, verbose_name='Временная метка')

    class Meta:
        verbose_name = 'Журнал действий'
        verbose_name_plural = 'Журнал действий'

    def __str__(self):
        return f'{self.user} - {self.action} - {self.timestamp}'

    @staticmethod
    def log_action(user, action):
        """
        Статический метод для логгирования действия.
        """
        ActivityLog.objects.create(user=user, action=action)
