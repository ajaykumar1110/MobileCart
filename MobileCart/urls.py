"""MobileCart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from stock import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('selling/', include('soldout.urls')),
    path('', views.home, name='home'),
        # Auth
    path('signup/', views.signupuser, name='signupuser'),
    path('login/', views.loginuser, name='loginuser'),
    path('logout/', views.logoutuser, name='logoutuser'),

    #stock
    path('stocklist/', views.stocklist, name='stocklist'),
    path('completed/', views.completedstocks, name='completedstocks'),
    path('addstocks/', views.addstocks, name='addstocks'),
    path('stock/<int:stock_pk>', views.viewstock, name='viewstock'),
    path('stock/<int:stock_pk>/complete', views.completedstock, name='completedstock'),
    path('stock/<int:stock_pk>/delete', views.deletestock, name='deletestock'),
    # path('seller/', views.seller, name='seller'), 
    path('issue_items/<str:stock_pk>/', views.issue_items, name="issue_items"),
    path('stock_detail/<int:stock_pk>/', views.stock_detail, name='stock_detail'),
    path('reorder_level/<int:stock_pk>/', views.reorder_level, name="reorder_level"),
    path('add_items/', views.add_items, name='add_items'),
    path('selling_history/', views.selling_history, name='selling_history'),
    path('deletecustomer/<int:sold_pk>', views.deletecustomer, name='deletecustomer'),
    path('trial/', views.trial, name='trial')
]
