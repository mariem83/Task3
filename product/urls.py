from django.urls import path
from rest_framework.authtoken import views
from product.views import productAPI, categoryAPI, allCategoriesAPI, allProductsAPI

urlpatterns = [
    path('products/<int:pk>', productAPI),
    path('categories/<int:pk>/products', allProductsAPI),
    path('categories', allCategoriesAPI),
    path('categories/<int:pk>', categoryAPI),
    path('api-token-auth/', views.obtain_auth_token),

]