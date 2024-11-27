from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('list-products/', views.list_products, name='list_products'),
    path('contact/', views.contact, name='contact'),
    path('sign-in/', views.sign_in, name='sign_in'),
    path('sign-up/', views.sign_up, name='sign_up'),
    path('details/<int:product_id>', views.details, name='details'),
]
