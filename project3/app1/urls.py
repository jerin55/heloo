from . import views
from django.urls import path

urlpatterns=[
    path('home',views.home,name='home'),
    path('Adminhome',views.Adminhome,name='Adminhome'),
    path('uslogin',views.uslogin,name='uslogin'),
    path('loginuser',views.loginuser,name='loginuser'),
    path('logout',views.logout,name='logout'),
    path('signup',views.signup,name='signup'),
    path('userceate',views.userceate,name='userceate'),
    path('addproduct',views.addproduct,name='addproduct'),
    path('addpr',views.addpr,name='addpr'),
    path('prodes/<int:pk>',views.prodes,name='prodes'),
    path('addcart/<int:pk>',views.addcart,name='addcart'),
    path('nw',views.nw,name='nw'),
    path('orderlist',views.orderlist,name='orderlist'),
    path('admincart',views.admincart,name='admincart'),
    path('users',views.users,name='users'),
    path('deluser/<int:pk>',views.deluser,name='deluser'),
    path('deleteuser/<int:pk>',views.deleteuser,name='deleteuser'),
    path('er',views.er,name='er')
    
]