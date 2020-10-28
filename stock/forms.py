from django.forms import ModelForm
from .models import Stock
from .models import Sold

class StockForm(ModelForm):
    class Meta:
        model = Stock
        fields = ['product', 'model', 'quantity','important']

    # def clean_product(self):
    # 	product = self.cleaned_data.get('product')
    # 	if not product:
    # 		raise form.ValidationError('This field is required')
    # 	return product
    # def clean_model(self):
    # 	model = self.cleaned_data.get('model')
    # 	if not model:
    # 		raise form.ValidationError('This field is required')
    # 	return model

class SoldForm(ModelForm):
    class Meta:
        model = Sold
        fields = ['customer_name','product', 'model', 'quantity']

class StockCreateFormBasic(ModelForm):
   class Meta:
     model = Stock
     fields = ['product', 'model', 'quantity']		

class StockSearchForm(ModelForm):
   class Meta:
     model = Stock
     fields = ['product', 'model']

class StockCreateForm(ModelForm):
	class Meta:
		model = Stock
		fields = ['product', 'model', 'quantity','dateReceived']

	def clean_product(self):
		product = self.cleaned_data.get('product')
		if not product:
			raise forms.ValidationError('This field is required')
		return product


	def clean_model(self):
		model = self.cleaned_data.get('model')
		if not model:
			raise forms.ValidationError('This field is required')
		return model

class IssueForm(ModelForm):
	class Meta:
		model = Stock
		fields = ['product','model','quantity']

class IssueForm1(ModelForm):
	class Meta:
		model = Stock
		fields = ['product','model','customer_name','issue_quantity']

class ReorderLevelForm(ModelForm):
	class Meta:
		model = Stock
		fields = ['reorder_level']

class SellForm(ModelForm):
	class Meta:
		model = Stock
		fields = ['customer_name','customer_product','customer_model','issue_quantity','address']

class SellFormSold(ModelForm):
	class Meta:
		model = Sold
		fields = ['customer_name','issue_quantity','address']

# class ReceiveForm(forms.ModelForm):
# 	class Meta:
# 		model = Sold
# 		fields = ['receive_quantity', 'receive_by']