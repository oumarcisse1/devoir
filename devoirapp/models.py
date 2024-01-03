from django.db import models

# Create your models here.
class Produits(models.Model):
    image = models.ImageField(blank=True, upload_to='images/')
    