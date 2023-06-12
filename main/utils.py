from .models import Product
from django.shortcuts import render, redirect
from django.contrib import messages


def search(request):
    if request.POST.get('search'):
        data = request.POST.get('search')
        try:
            print('try')
            products = Product.objects.get(title=data)
            context = {
                'products': products
            }
            print(products)
            return render(request, 'main/search_result.html', context)
        except:
            print('except')
            messages.error(request, 'Ничего не найдено...')
            return redirect('search')
    else:
        pass
