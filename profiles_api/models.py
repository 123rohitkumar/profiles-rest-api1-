from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.
class UserProfileManager(BaseUserManager):
    """Create a manager for user profile"""

    def create_user(self,email,name,password=None):
        """create a new user """
        if not email:
            raise ValueError('User must have an email Address')

        email=self.normalize_email(email)
        user=self.model(email=email,name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def Create_Superuser(self,email,name,password):
        """Create and save a new super user with given detais"""
        user=create_user(email,name,password)

        user.is_superuser=True
        user.is_active=True
        user.save(using=self._db)

        return user

class UserProfile(AbstractBaseUser,PermissionsMixin):
    """Database model for user in system"""

    email=models.EmailField(max_length=255,unique=True)
    name=models.CharField(max_length=255)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=True)

    objects=UserProfileManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELD=['name']

    def get_full_name(self):
        """retrive full name of user"""
        return self.name

    def get_short_name(name):
        """retrive short name"""
        return self.name

    def __str__(self):
        """string representation of our user"""
        return self.email
