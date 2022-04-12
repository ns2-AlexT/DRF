from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    redefine the email field as unique
    """
    e_mail = models.EmailField('email address', unique=True)
