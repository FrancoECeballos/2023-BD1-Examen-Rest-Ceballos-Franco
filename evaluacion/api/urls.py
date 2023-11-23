from django.contrib import admin
from django.urls import path, include
from api import views

urlpatterns = [
    path('', views.empiezaCon),
    path('admin/', admin.site.urls),
    path('customers/', views.customers),
    path('customers/<str:pk>/', views.customers_id),
    path('categories/', views.categories),
    path('categories/<int:pk>/', views.categories_id),
    path('employees/', views.employees),
    path('employees/<int:pk>/', views.employees_id),
    path('orderDetails/', views.orderDetails),
    path('orderDetails/<int:pk1>/<int:pk2>/', views.orderDetails_id),
    path('orders/', views.orders),
    path('orders/<int:pk>/', views.orders_id),
    path('suppliers/', views.suppliers),
    path('suppliers/<int:pk>/', views.suppliers_id),
    path('products/', views.products),
    path('products/<int:pk>/', views.products_id),
    #Evaluación
    path('punto1/products', views.punto1),
    path('punto2/orders', views.punto2)
]
