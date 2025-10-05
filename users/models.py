# Create your models here.
from .managers import CustomUserManager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


class CustomUser(AbstractBaseUser, PermissionsMixin):
    class UserType(models.IntegerChoices):
        SUPERADMIN = 1, "SuperAdmin"
        USER = 2, "User"

    name = models.CharField(max_length=150)
    user_type = models.PositiveSmallIntegerField(
        choices=UserType.choices, default=UserType.USER
    )
    email = models.EmailField(
        unique=True,
        error_messages={
            "invalid": "Enter a valid email address.",
        },
    )
    age = models.IntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def __str__(self):
        return self.email
