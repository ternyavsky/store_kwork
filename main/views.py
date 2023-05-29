from django.shortcuts import render, redirect
from .models import Product, Category, Feedback, Question
from django.contrib import messages
from .cart import Cart
from yoomoney import Quickpay
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


def accept(request):
    return render(request,'platezhi/accept.html')
     

def decline(request):
    return render(request,'platezhi/decline.html')
    




# Create your views here.
def index(request):
    if request.method == 'GET':
        last_products = Product.objects.all().order_by('-pk')[:3]
        return render(request,'main/index.html',{'last_products':last_products})
    else:
        try:
            question = Question.objects.get(author=request.user)
            if question:
                messages.error(request,'Вы уже оставили обращение! Дождитесь ответа на текущее обращение чтобы создать следующее.')
                print('work try')
                return redirect('index')
                
        except:
            author = request.user
            text = request.POST.get('text')
            question = Question.objects.create(author=author,text=text)
            question.save()
            print('work except') 
            return redirect('index')
def page(request,id):
    products = Product.objects.filter(category=id)
    context = {
        'products':products
    }
    return render(request,'main/page.html',context)
#T7c7fPJc
#P1096489471
#юмани F3A904ECAA38E830320969772F6B2B43EBC99F7E6BB4AE78102E236529BC39B0
def single(request,product_id):
    if request.method == 'GET':
        product = Product.objects.get(id=product_id)
        feedback = Feedback.objects.filter(product=product_id)
        context = {
            'product':product,
            'feedbacks':feedback
        }
        return render(request,'main/productcard.html',context)
    else:
        try:
            feedback = Feedback.objects.get(author=request.user, product=product_id)
            if feedback:
                messages.error(request,'Вы уже оставили отзыв к этому товару!')
                print('work try')
                return redirect('single',product_id)
        except:
            author = request.user
            text = request.POST.get('text')
            product = Product.objects.get(id=product_id)
            feedback = Feedback.objects.create(author=author,text=text,product=product)
            feedback.save()
            print('work except') 
            return redirect('single',product_id)
        
        

def buy(request):
    total = Cart(request).get_total_price()
    if int(total) > 14999:
        print(int(total))
        messages.error(request,'Максимальная сумма одного заказа не более 15.000₽')
        return redirect('cart')
    else:
        quickpay = Quickpay(
                receiver="410011820942473",
                quickpay_form="shop",
                targets="Оплата товара",
                paymentType="SB",
                sum=total)
        return redirect(quickpay.redirected_url)

def single_buy(request,product_id):
    product = Product.objects.get(id=product_id)
    total=int(product.price)
    quickpay = Quickpay(
                receiver="410011820942473",
                quickpay_form="shop",
                targets="Оплата товара",
                paymentType="SB",
                sum=total)
    return redirect(quickpay.redirected_url)


# Add item's quantity from cart 
@login_required
def move_add(request,product_id):
    item = Product.objects.get(id=product_id)
    cart = Cart(request)
    cart.move_add(product=item)
    return redirect('cart')


# Remove item's quantity from cart


@login_required
def move_remove(request,product_id):
    item = Product.objects.get(id=product_id)
    cart = Cart(request)
    cart.move_remove(product=item)
    return redirect('cart')

@login_required
def cart_add(request,product_id):
    item = Product.objects.get(id=product_id)
    cart = Cart(request)
    cart.add(request=request,product=item)
    return redirect('page',item.category.id)

def cart(request):
    cart = Cart(request)
    return render(request,'main/cart.html',{'cart':cart})

