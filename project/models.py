from django.db import models

# Create your models here.

class Client(models.Model):
    dni = models.CharField(max_length=12)
    name = models.CharField(max_length=60)
    adress = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)


class Product(models.Model):
    name = models.CharField(max_length=60)


class Invoice(models.Model):
    reg = models.CharField(max_length=6)
    date = models.DateField(auto_now=True)
    state = models.CharField(max_length=30)
    finance = models.IntegerField()
    id_client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)


class Detail(models.Model):
   price = models.FloatField()
   amount = models.IntegerField()
   id_product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
   id_invoice = models.ForeignKey(Invoice, on_delete=models.SET_NULL, null=True)


class Payments(models.Model):
    input_money = models.FloatField()
    date_prog = models.DateField()
    date_input = models.DateField(auto_now=True)
    id_invoice = models.ForeignKey(Invoice, on_delete=models.SET_NULL, null=True)

