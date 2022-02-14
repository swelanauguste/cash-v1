from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
# from django.urls import reverse


class User(AbstractUser):
    is_cashier = models.BooleanField(default=True)
    is_approver = models.BooleanField(default=False)
    is_cash_production = models.BooleanField(default=False)


GENDER_LIST = [
    ("M", "M"),
    ("F", "F"),
]


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    first_name = models.CharField(max_length=65, blank=True)
    last_name = models.CharField(max_length=65, blank=True)
    slug = models.SlugField(max_length=65, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_LIST)
    dob = models.DateField(blank=True, null=True)
    bio = models.TextField(blank=True)
    phone = models.CharField(max_length=25, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)
        super(UserProfile, self).save(*args, **kwargs)

    def __str__(self) -> str: 
        return self.user.username