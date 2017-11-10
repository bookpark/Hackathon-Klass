from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(null=False, blank=False)
    is_active = models.BooleanField(
        default=False,
    )

