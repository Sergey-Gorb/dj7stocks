from rest_framework.viewsets import ModelViewSet
from .models import Product, Stock
from .serializers import ProductSerializer, StockSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_fields = ('title', 'description', )


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    search_fields = ('products__title',)