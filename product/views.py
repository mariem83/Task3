from Task3.authentication import CustomAuth
from .models import Product, Category
from .serializers import ProdSer, CategorySer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated



class ProductView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProdSer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated]
    authentication_classes = [CustomAuth]

class CategoryView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated]
    authentication_classes = [CustomAuth]

class CategoriesView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySer
    permission_classes = [IsAuthenticated]
    authentication_classes = [CustomAuth]


class ProductsView(generics.ListAPIView):
    serializer_class = ProdSer
    permission_classes = [IsAuthenticated]
    authentication_classes = [CustomAuth]

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Product.objects.filter(category_id=pk)



allCategoriesAPI = CategoriesView.as_view()
allProductsAPI = ProductsView.as_view()
productAPI = ProductView.as_view()
categoryAPI = CategoryView.as_view()

# Create your views here.
