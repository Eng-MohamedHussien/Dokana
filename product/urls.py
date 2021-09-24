from django.urls import path
from . import views

app_name = 'product' 

urlpatterns = [
    path('', views.home, name='home'),
    path('Categories/<str:category_slug>/', views.show_category_items, name='show_category_items'),
    path('Products/<str:product_slug>/', views.product_details, name='product_details'),
    path('Dokana/login/', views.open_dokana, name='open_dokana'),
    path('discounts/', views.show_discounts, name='show_discounts'),
    path('discounts/<str:category_slug>/', views.show_discounts_per_category, name='show_discounts_per_category')
]
