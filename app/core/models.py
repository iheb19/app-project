from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
class UserManager(BaseUserManager):
    "manage for users"
    def create_user(self, email, password=None, **extra_fields):
        """create save return new user"""
        user=self.model(email=email, **extra_fields)
        user.setpassword(password)
        user.save(using=self._db)
        return user
class User(AbstractBaseUser, PermissionsMixin):
    """user in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    object = UserManager()
    USERNAME_FIELD = 'email'
