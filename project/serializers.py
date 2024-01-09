from rest_framework import serializers
from .models import Client
from .models import Product
from .models import Invoice
from .models import Detail
from .models import Payments

class Client_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"


class Product_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        

class Invoice_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = "__all__"
        

class Detail_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Detail
        fields = "__all__"
        

class Payments_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = "__all__"
