from django.db import models
from django.contrib.auth.models import User
# from phonenumber_field.modelfields import phoneNumberField

class Sold(models.Model):
    product = models.CharField(max_length=50)
    model = models.CharField(max_length=50,blank=True)
    # phone = phoneNumberField(null=False,blank=False,unique=True)
    receivedTime = models.DateTimeField(auto_now_add=True)
    dateReceived = models.DateTimeField(null=True, blank=True)
    quantity = models.IntegerField(default=False)
    customer_name = models.CharField(max_length=50)
    purchaser_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.customer_name