from django.urls import path
from . import views

urlpatterns = [
    path('lessons/', views.LessonsList.as_view(), name='lessons'),
    path('products/', views.ProductList.as_view(), name='products_list'),
    path('products/statistic/', views.ProductStatistic.as_view(), name='product_detail'),
    path('products/<pk>/', views.ProductDetail.as_view(), name='product'),
]
