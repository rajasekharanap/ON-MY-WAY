from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    username = None
    fullname = models.CharField(max_length=255, blank=False)
    email = models.EmailField(_('email address'), unique=True)
    phone = models.TextField(max_length=20, default=0)
    usertype = models.CharField(max_length=20, default='passenger')
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD ='email'
    REQUIRED_FIELDS = ['phone', 'fullname']

    def __str__(self):
        return self.email

class UserFiles(models.Model):
    userfile = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True, related_name='userfiles')
    govtid = models.FileField(upload_to='govtid', null=True)
    license = models.FileField(upload_to='license', null=True)
    vehiclecertificate = models.FileField(upload_to='vehiclecertificate', null=True)