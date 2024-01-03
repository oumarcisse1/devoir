from django.contrib import admin
from .models import Produits

# Register your models here.
# Register your models here.
import admin_thumbnails


@admin_thumbnails.thumbnail('image')

class AdminProduit(admin.ModelAdmin):
    list_display = ('image_thumbnail')
   
admin.site.register(Produits)