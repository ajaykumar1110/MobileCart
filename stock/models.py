from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import datetime

class Stock(models.Model):
    product = models.CharField(max_length=50,blank=False,null=True)
    model = models.CharField(max_length=50,blank=True,null=True)
    received = models.DateTimeField(auto_now_add=False, auto_now=True)
    dateReceived = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    quantity = models.IntegerField(default='0',blank=True,null=True)
    customer_name = models.CharField(max_length=50,blank=False,null=True)
    customer_product = models.CharField(max_length=50,blank=True,null=True)
    customer_model = models.CharField(max_length=50,blank=True,null=True)
    address = models.TextField(max_length=50,blank=True,null=True)
    date = models.DateTimeField(auto_now_add=False, auto_now=True)
    issue_quantity=models.IntegerField(default='0',blank=True,null=True)
    receive_quantity=models.IntegerField(default='0',blank=True,null=True)
    reorder_level=models.IntegerField(default='0',blank=True,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(Stock):
        return Stock.product

class Sold(models.Model):
    product = models.CharField(max_length=50)
    model = models.CharField(max_length=50,blank=True)
    # phone = phoneNumberField(null=False,blank=False,unique=True)
    receivedTime = models.DateTimeField(auto_now_add=True)
    dateReceived = models.DateTimeField(null=True, blank=True)
    quantity = models.IntegerField(default=False)
    customer_name = models.CharField(max_length=50)
    customer_product = models.CharField(max_length=50,blank=True,null=True)
    customer_model = models.CharField(max_length=50,blank=True,null=True)
    address = models.TextField(max_length=50,blank=True,null=True)
    issue_quantity=models.IntegerField(default='0',blank=True,null=True)
    # issued_by=models.CharField(max_length=50,blank=True,null=True)

    def __str__(Sold):
        return Sold.customer_name

    
