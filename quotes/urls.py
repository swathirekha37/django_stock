from django.urls import path
from .views import home,about,add_stock,delete,delete_stock

urlpatterns = [
   path('',home,name='home'),
   path('about/',about,name='about'),
   path('add_stock/',add_stock,name='add_stock'),
   path('delete/<id>',delete,name='delete'),
   path('delete_stock',delete_stock,name='delete_stock')
]