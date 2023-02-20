from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.core.mail import send_mail
from django.db import models
from django.urls import reverse


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, username, password, **extra_fields):
        '''
        Создает и сохраняет пользователя с введенной почтой,
        именем пользователя и паролем.
        '''
        if not email:
            raise ValueError('email должен быть указан')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_staff', False)
        return self._create_user(email, username, password, **extra_fields)

    def create_superuser(self, email, username, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')

        return self._create_user(email, username, password, **extra_fields)

    def actived(self):
        return self.get_queryset().filter(is_active=True)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('почта', unique=True)

    username = models.CharField('имя пользователя', max_length=50)

    is_staff = models.BooleanField(
        'статус персонала', default=False,
        help_text='Определяет доступ пользователя к админ панели',
        )
    is_active = models.BooleanField('активен', default=True)

    date_joined = models.DateTimeField('дата регистрации', auto_now_add=True)

    objects = UserManager()

    chat_id = models.IntegerField('chat_id пользователя', default=0)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return self.username

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def get_absolute_url(self):
        return reverse('users:user_details', kwargs={'user_id': self.pk})
