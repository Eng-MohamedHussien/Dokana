from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        max_length=255,
        unique=True,
        verbose_name='البريد الالكترونى'
    )
    name = models.CharField(max_length= 255, verbose_name='الاسم')
    mobile_number = models.CharField(max_length=11, verbose_name='رقم الموبايل')
    another_mobile = models.CharField(max_length=11, blank=True, null=True, verbose_name='رقم بديل')
    is_active = models.BooleanField(default=True, verbose_name='تفعيل الحساب')
    is_staff = models.BooleanField(default=False, verbose_name='مستخدم')
    is_superuser = models.BooleanField(default=False, verbose_name='ادمين')
    created = models.DateTimeField(auto_now_add=True, verbose_name='توقيت التسجيل')
    updated = models.DateTimeField(auto_now=True, verbose_name='توقيت اخر تعديل')

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = 'مستخدم'
        verbose_name_plural = "المستخدمون"

    def __str__(self):
        return self.email