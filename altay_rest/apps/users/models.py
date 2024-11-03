from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager
from django.core.validators import RegexValidator



class UserManager(BaseUserManager):
    """
    Менеджер модели User.
    """

    def create_superuser(self, username: str, password: str) -> AbstractUser:
        """

        """
        if not username:
            raise ValueError('Email пользователя не может быть пустым')

        user = self.model(username=username)
        user.set_password(password)
        user.is_superuser = True
        user.is_admin = True
        user.is_active = True
        user.first_name = 'Altay'
        user.last_name = "Rest"
        user.second_name = 'admin'
        user.save(using=self._db)
        return user


class User(AbstractUser, PermissionsMixin):
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    username = models.EmailField(
        verbose_name='Email',
        help_text='Email пользователя',
        max_length=32,
        unique=True
    )
    update_username = models.EmailField(
        verbose_name='Новый email',
        help_text='Email',
        max_length=32,
        unique=True,
        blank=True,
        null=True
    )
    first_name = models.CharField(
        verbose_name='Имя',
        help_text='Имя пользователя',
        max_length=255,
        default=''
    )
    surname = models.CharField(
        verbose_name='Отчество',
        help_text='Отчество',
        max_length=255,
        default=''
    )
    last_name = models.CharField(
        verbose_name='Фамилия',
        help_text='Фамилия пользователя',
        max_length=255,
        default=''
    )
    status = models.CharField(
        verbose_name='Статус',
        help_text='Статус пользователя',
        default=False,
        max_length=255,
        blank=True,
        null=True,
    )
    objects = UserManager()
    USERNAME_FIELD = 'username'