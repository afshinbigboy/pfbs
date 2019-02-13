
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
import uuid
import requests
import datetime
from datetime import date
from pytz import UTC
from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed



class UserAccountManager(BaseUserManager):
    use_in_migrations = True
 
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Email address must be provided')
        if not password:
            raise ValueError('Password must be provided')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
 
    def create_user(self, email=None, password=None, **extra_fields):
        return self._create_user(email, password, **extra_fields)
 
    def create_superuser(self, email, password, **extra_fields):
        extra_fields['is_staff'] = True
        extra_fields['is_superuser'] = True
 
        return self._create_user(email, password, **extra_fields)



class User(AbstractBaseUser, PermissionsMixin):
 
    REQUIRED_FIELDS = ['std_id', 'first_name', 'last_name', 'gender', 'grade', 'email']
    USERNAME_FIELD = 'username'
 
    objects = UserAccountManager()
 
    email = models.EmailField('email address', max_length=255, unique=True)
    username = models.CharField('username', max_length=40, unique=True)
    std_id = models.CharField('student ID', max_length=9, unique=True)
    
    first_name = models.CharField('first name', max_length=60)
    last_name = models.CharField('last name', max_length=60)

    GENDER_CHOICES = (
        ("M", "Male"),
        ("F", "Female"),
    )
    GRADE_CHOICES = (
        ("M", "MSc"),
        ("P", "PhD"),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    grade = models.CharField(max_length=1, choices=GRADE_CHOICES)


    # System control fields
    is_staff = models.BooleanField('staff status', default=False)
    is_admin = models.BooleanField('admin status', default=False)
    is_active = models.BooleanField('active', default=True)
    is_blocked = models.BooleanField('blocked', default=False)

    is_teacher = models.BooleanField('teacher', default=False)
    
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def get_short_name(self):
        return (self.first_name[0]+self.last_name[0]).upper()
 
    def get_full_name(self):
        return self.first_name.capitalize()+' '+self.last_name.capitalize()

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)
    
    def __unicode__(self):
        return self.email

