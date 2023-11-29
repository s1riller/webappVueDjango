from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from django.contrib.auth import get_user_model


class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_active', 'is_staff','confirmation_token')
    search_fields = ('email', 'first_name', 'last_name', 'confirmation_token')
    ordering = ('email',)  # Use 'email' instead of 'username' in the ordering attribute
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'avatar')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )


admin.site.register(get_user_model(), CustomUserAdmin)


class SoftDeleteRestoreAdminMixin:
    actions = ['soft_delete_selected', 'restore_selected']

    def soft_delete_selected(self, request, queryset):
        for obj in queryset:
            obj.soft_delete()

    soft_delete_selected.short_description = 'Мягкое удаление выбранных объектов'

    def restore_selected(self, request, queryset):
        for obj in queryset:
            obj.restore()

    restore_selected.short_description = 'Восстановление выбранных объектов из мусорной корзины'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin, SoftDeleteRestoreAdminMixin):
    list_display = ('name', 'price', 'stock_quantity', 'category', 'created_at', 'updated_at', 'is_deleted')
    list_filter = ('category', 'is_deleted')

    # Важно добавить следующие две строки
    actions = SoftDeleteRestoreAdminMixin.actions
    soft_delete_selected = SoftDeleteRestoreAdminMixin.soft_delete_selected
    restore_selected = SoftDeleteRestoreAdminMixin.restore_selected


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product',)
    list_filter = ('product',)


@admin.register(TrashBin)
class TrashBinAdmin(admin.ModelAdmin, SoftDeleteRestoreAdminMixin):
    list_display = ('product', 'deleted_at',)
    list_filter = ('product', 'deleted_at',)

    # Важно добавить следующие две строки
    actions = SoftDeleteRestoreAdminMixin.actions
    soft_delete_selected = SoftDeleteRestoreAdminMixin.soft_delete_selected
    restore_selected = SoftDeleteRestoreAdminMixin.restore_selected


@admin.register(ActivityLog)
class ActivityLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'action', 'timestamp',)
    list_filter = ('user', 'action', 'timestamp',)
