from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('reg',views.signup),
    path('login',views.signin),
    path('users',views.user),
    path('edit/<int:pk>',views.edit,name='edit'),
    path('delete/<int:pk>',views.delete,name='delete'),
    path('pet',views.pets),
    path('allpet',views.allpets),
    path('addtocart/<int:pid>',views.addtocart,name='cart'),
    path('viewcart',views.viewcart),
    path('cartitem_delete/<int:cid>',views.cartitem_delete,name='cartdelete'),
    path('sendmail',views.sendmail),
    path('formview',views.formview)
]