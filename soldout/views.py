from django.shortcuts import render, redirect, get_object_or_404
from stock.forms import StockForm
from stock.models import Stock
from .forms import SoldForm
from .models import Sold
from django.contrib.auth.models import User
from django.utils import timezone
from stock.views import userid
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
	if request.method == 'GET':
		Stocks = Stock.objects.all()
		print('here1')
		return render(request, 'sold/home.html', {'Stock':Stocks})
	else:
		try:
			form = SoldForm(request.POST)
			newtodo = form.save(commit=False)
			newtodo.user = userid()
			newtodo.save()
			return redirect('trial')
		except ValueError:
			print('here2')
			return render(request, 'sold/home.html', {'form':SoldForm(), 'error':'Bad data passed in. Try again.'})

@login_required
def trial(request):
	string=request.GET.get('Product')
	return render(request, 'sold/trial.html', {'str': string})