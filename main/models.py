from django.db import models
from oauth.models import User

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    text = models.TextField(max_length=1000)
    image = models.ImageField(default=None, blank=True,upload_to='pictures/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    
class Question(models.Model):
    author = models.ForeignKey(User,on_delete=models.PROTECT, null=True, blank=True)
    text = models.TextField(max_length=1000)

    def __str__(self):
        return f'{self.author} - {self.text}'

class Feedback(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    text = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.author} - {self.text}'
