# ваш_проект/views.py
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from django.utils.translation import gettext as _
from djangoapp.settings import APP_FRONTEND_DOMAIN

class CustomUserCreateView(APIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = get_user_model().objects.create_user(**serializer.validated_data)



            # Генерация токена подтверждения
            confirmation_token = user.generate_confirmation_token()

            # Формирование ссылки для подтверждения
            confirmation_link = f"{APP_FRONTEND_DOMAIN}confirm-registration/{confirmation_token}/"
            # Отправка письма на почту пользователя
            send_mail(
                subject=_("Пожалуйста, подтвердите регистрацию!"),
                message=_("Перейдите по этой ссылке для подтверждения регистрации: ") + confirmation_link,
                from_email="miheevsaveliy@yandex.ru",
                recipient_list=[user.email]
            )

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ConfirmRegistrationView(generics.GenericAPIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, token):
        # Попытка найти пользователя с соответствующим токеном подтверждения
        try:
            user = get_user_model().objects.get(confirmation_token=token, is_active=False)
        except get_user_model().DoesNotExist:
            return Response({'detail': _('Пользователь не найден.')}, status=status.HTTP_404_NOT_FOUND)

        # Подтверждение регистрации пользователя
        user.is_active = True
        user.confirmation_token = ''
        user.save()

        return Response({'detail': _('Ваша регистрация успешно подтверждена!')}, status=status.HTTP_200_OK)