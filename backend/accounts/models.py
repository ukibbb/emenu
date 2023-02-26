import logging
import uuid

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models

logger = logging.getLogger(__name__)


class UserManager(BaseUserManager):
    def _create_user(
        self,
        email,
        password,
        is_staff,
        is_superuser,
        **extra_fields,
    ):
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email, password, **extra_fields):
        return self._create_user(
            email,
            password,
            is_staff=False,
            is_superuser=False,
            **extra_fields,
        )

    def create_superuser(self, email, password=None, **extra_fields):
        return self._create_user(
            email,
            password,
            is_staff=True,
            is_superuser=True,
            **extra_fields,
        )


class User(AbstractBaseUser, PermissionsMixin):
    app_label = "accounts"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    email = models.EmailField(unique=True)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "email"

    objects = UserManager()

    def __str__(self):
        return f"{self.id} - {self.email}"
