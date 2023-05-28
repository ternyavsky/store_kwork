from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    photo = models.ImageField(upload_to='users/%Y/%m/%d',blank=True)


    @property
    def user_image(self):
        try:
            url = self.photo.url
        except:
            url = ''
        return url