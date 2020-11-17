from django.db import models

from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,PermissionsMixin)

class UserManager(BaseUserManager):
    def create_user(self, username, email, phone, password=None):
        if username is None:
            raise TypeError('Users should have username')
        if email is None:
            raise TypeError('Users should have email')
        if phone is None:
            raise TypeError('Users should have phone')
        user = self.model(username=username,phone=phone,email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self, username, email,phone, password=None):
        if username is None:
            raise TypeError('Users should have username')
        if email is None:
            raise TypeError('Users should have email')
        if phone is None:
            raise TypeError('Users should have phone')
        user = self.create_user(username,email,phone,password) #map to create_user function by using self in oop feature
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True, db_index=True)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    phone = models.CharField(max_length=255,unique=True,db_index=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','phone']

    objects = UserManager()
    def __str__(self):
        return self.email
    def tokens(self):
        return ''