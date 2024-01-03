from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
     produits_object = Produits.objects.all()
     item_name = request.GET.get('item-name')
     if item_name !='' and item_name is not None:
        produits_object = Produits.objects.filter(titre__icontains=item_name)
   
     return render(request, 'devoirapp/index.html', {'produits_object': produits_object})



def contact(request):
    return render(request, 'devoirapp/contact.html')
