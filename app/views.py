from django.shortcuts import render, HttpResponse
from .models import Product
from django.views import View
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Q

# def home(request):
#  return render(request, 'app/home.html')

class ProductView(View):
    def get(self, request):
        Living = Product.objects.filter(category='L')
        Bedroom = Product.objects.filter(category='B')
        Dining = Product.objects.filter(category='D')
        Storage= Product.objects.filter(category='S')
        Study = Product.objects.filter(category='ST')
        Decor = Product.objects.filter(category='DE')

        Cat = { 'Living':Living, 
                'Bedroom':Bedroom, 
                'Dining':Dining, 
                'Storage':Storage,
                'Study':Study,
                'Decor':Decor,
                }
        return render(request, 'app/home.html', Cat)

#def product_detail(request):
#  return render(request, 'app/productdetail.html')

class ProductDetailView(View):
        def get(self, request, pk):
                product = Product.objects.get(pk=pk)
                print(product.id)
                return render(request, 'app/productdetail.html', {'product':product})

# def Living(request):
#  return render(request, 'app/living.html')

def Living(request, data=None):
        if data==None :
                Living = Product.objects.filter(category='L')
        elif data == 'Sofa' or data == 'Corner':
                Living= Product.objects.filter(category='L').filter(type=data)
        elif data == 'Wooden' or data == 'Lovesit':
                Living= Product.objects.filter(category='L').filter(type=data)
        elif data == 'Wooden' or data == 'Loveseats':
                Living= Product.objects.filter(category='L').filter(type=data)
        elif data == 'futons' or data == 'Chaire':
                Living= Product.objects.filter(category='L').filter(type=data)
        elif data == 'Coffe-table' :
                Living= Product.objects.filter(category='L').filter(type=data)
        return render(request, 'app/living.html', {'Living':Living})