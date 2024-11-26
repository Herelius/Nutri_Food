from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('list-products/', views.list_products, name='list_products'),
    path('contact/', views.contact, name='contact'),
    path('details/<int:product_id>', views.contact, name='detail'),
]
