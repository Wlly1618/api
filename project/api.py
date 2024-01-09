from rest_framework import viewsets, permissions
from .serializers import Client_Serializer
from .serializers import Product_Serializer
from .serializers import Invoice_Serializer
from .serializers import Detail_Serializer
from .serializers import Payments_Serializer
from .models import Client
from .models import Product
from .models import Invoice
from .models import Detail
from .models import Payments


class Client_viewset(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Client_Serializer


class Product_viewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Product_Serializer


class Invoice_viewset(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Invoice_Serializer


class Detail_viewset(viewsets.ModelViewSet):
    queryset = Detail.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Detail_Serializer


class Payments_viewset(viewsets.ModelViewSet):
    queryset = Payments.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Payments_Serializer
