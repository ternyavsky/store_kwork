from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('',views.index,name = 'index'),
    path('items/<str:id>/',views.page,name= 'page'),
    path('product/<int:product_id>',views.single,name='single'),
    path('cart/',views.cart,name= 'cart'),
    path('cart_add<int:product_id>',views.cart_add,name='cart_add'),
    path('add<int:product_id>',views.move_add,name='move_add'),
    path('remove<int:product_id>',views.move_remove,name='move_remove'),
    path('buy',views.buy,name='buy'),
    path('accept',views.accept,name='accept'),
    path('decline',views.decline,name='decline'),
    path('buy<int:product_id>',views.single_buy,name='single_buy'),


]   