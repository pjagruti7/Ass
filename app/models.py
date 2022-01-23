from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

CATEGORY_CHOICES = (
 ('L', 'Living'),
 ('B', 'Bedroom'),
 ('D', 'Dining'),
 ('S', 'Storage'),
 ('ST', 'Study'),
 ('DE', 'Decor'),
)
class Product(models.Model):
 title = models.CharField(max_length=100)
 price = models.FloatField()
 type = models.CharField(max_length=100)
 category = models.CharField( choices=CATEGORY_CHOICES, max_length=2)
 product_image = models.ImageField(upload_to='productimg')

 def __str__(self):
  return str(self.id)


