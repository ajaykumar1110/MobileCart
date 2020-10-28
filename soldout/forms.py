from django.forms import ModelForm
from .models import Sold
# from phonenumber_field.formfields import phoneNumberField

# class Client(forms.Form):
# 	phone = phoneNumberField()

class SoldForm(ModelForm):
    class Meta:
        model = Sold
        fields = ['customer_name','product', 'model', 'quantity', 'dateReceived']