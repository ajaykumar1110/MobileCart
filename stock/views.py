from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import *
from .models import Stock
from .forms import SoldForm
from .models import Sold
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def home(request):
    return render(request, 'stock/home.html')

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'stock/signupuser.html', {'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('stocklist')
            except IntegrityError:
                return render(request, 'stock/signupuser.html', {'form':UserCreationForm(), 'error':'That username has already been taken. Please choose a new username'})
        else:
            return render(request, 'stock/signupuser.html', {'form':UserCreationForm(), 'error':'Passwords did not match'})

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'stock/loginuser.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'stock/loginuser.html', {'form':AuthenticationForm(), 'error':'Username and password did not match'})
        else:
            login(request, user)
            return redirect('stocklist')

# @login_required
# def addstocks(request):
#     if request.method == 'GET':
#         return render(request, 'stock/addstocks.html', {'form':IssueForm()})
#     else:
#         try:
#             form = IssueForm(request.POST)
#             newtodo = form.save(commit=False)
#             newtodo.user = request.user
#             newtodo.date = timezone.now()
#             newtodo.save()
#             contexts = {
#                 "form": form,
#             }
#             return render(request, 'stock/stocklist.html', {'contexts':contexts})
#             # return redirect('stocklist')
#         except ValueError:
#             return render(request, 'stock/addstocks.html', {'form':IssueForm(), 'error':'Bad data passed in. Try again.'})
@login_required
def addstocks(request):
    if request.method == 'GET':
        return render(request, 'stock/addstocks.html', {'form':StockForm()})
    else:
        try:
            form = StockForm(request.POST)
            newtodo = form.save(commit=False)
            newtodo.user = request.user
            newtodo.save()
            return redirect('stocklist')
        except ValueError:
            return render(request, 'stock/stocklist.html', {'form':StockForm(), 'error':'Bad data passed in. Try again.'})

@login_required
def viewstock(request, stock_pk):
    stock = get_object_or_404(Stock, pk=stock_pk, user=request.user)
    if request.method == 'GET':
        form = StockForm(instance=stock)
        return render(request, 'stock/viewstock.html', {'stock':stock, 'form':form})
    else:
        try:
            form = StockForm(request.POST, instance=stock)
            form.save()
            # return render(request,'stock/stocklist.html')
            return redirect('stocklist')
        except ValueError:
            return render(request, 'stock/viewstock.html', {'stock':stock, 'form':form, 'error':'Bad info'})


@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

@login_required
def stocklist(request):
    form = StockSearchForm(request.POST or None)
    contexts = Stock.objects.filter(user=request.user)
    if request.method == 'POST':
        contexts = Stock.objects.filter(product__icontains=form['product'].value(),
                                        model__icontains=form['model'].value()
                                        )
    return render(request, 'stock/stocklist.html', {'contexts':contexts,"form": form})

@login_required
def trial(request):
    return render(request, 'stock/trial.html')

@login_required
def completedstocks(request):
    Stocks = Stock.objects.filter(user=request.user, date__isnull=False).order_by('-date')
    return render(request, 'stock/completedstocks.html', {'stocks':Stocks})

@login_required
def deletestock(request, stock_pk):
    stock = get_object_or_404(Stock, pk=stock_pk, user=request.user)
    if request.method == 'POST':
        stock.delete()
        return redirect('stocklist')
    return render(request, 'stock/delete_items.html')

# def delete_items(request):
#     return render(request, 'delete_items')


@login_required
def completedstock(request, stock_pk):
    stock = get_object_or_404(Stock, pk=stock_pk, user=request.user)
    if request.method == 'POST':
        # stock.dateReceived = timezone.now()
        stock.save()
        return redirect('stocklist')

@login_required
def userid():
    return request.user

# @login_required
# def seller(request, stock_pk):
#     queryset = Stock.objects.get(id=stock_pk)
#     form = SellForm(request.POST or None, instance=queryset)
#     if form.is_valid():
#         form.save()
#         instance = form.save(commit=False)
#         instance.issue_quantity = (instance.quantity)-(instance.issue_quantity)
#         quant=instance.quantity
#         prod=instance.product
#         messages.success(request, "ISSUED SUCCESSFULLY----------" + "     " + str(quant) + "  " + str(prod) + " products now left in Store")
#         instance.save()
#         return render(request,'stock/stock_detail.html',{'queryset':queryset})
#     context = {
#         "title": 'Issue ' + str(queryset.product),
#         "queryset": queryset,
#         "quantity":queryset.quantity,
#         "form": form,
#         "username": 'Issue By: ' + str(request.user),
#     }
#     return render(request, 'stock/add_item.html', context)

@login_required
def trial(request):
    string=request.GET.get('Product')
    return render(request, 'stock/trial.html', {'str': string})
# Main
# @login_required
# def issue_items(request, stock_pk):
#     queryset = Stock.objects.get(id=stock_pk)
#     form = IssueForm1(request.POST or None, instance=queryset)
#     if form.is_valid():
#         form.save()
#         instance = form.save(commit=False)
#         instance.quantity = (instance.quantity)-(instance.issue_quantity)
#         quant=instance.quantity
#         prod=instance.product
#         messages.success(request, "ISSUED SUCCESSFULLY----------" + "     " + str(quant) + "  " + str(prod) + " products now left in Store")
#         instance.save()
#         return render(request,'stock/stock_detail.html',{'queryset':queryset})
#     context = {
#         "title": 'Issue ' + str(queryset.product),
#         "queryset": queryset,
#         "quantity":queryset.quantity,
#         "form": form,
#         "username": 'Issue By: ' + str(request.user),
#     }
#     return render(request, 'stock/add_item.html', context)


@login_required
def issue_items(request, stock_pk):
    querysetsold = Sold.objects.all()
    queryset = Stock.objects.get(id=stock_pk)
    #
    form = SellForm(request.POST or None, instance=queryset)
    formSold = SellFormSold(request.POST or None)
    #
    if form.is_valid():
        form.save()
        formSold.save()
        #
        instance = form.save(commit=False)
        instancesold = formSold.save(commit=False)
        #   
        instance.quantity = (instance.quantity)-(instance.issue_quantity)
        #
        instancesold.customer_model=queryset.model
        instancesold.customer_product=queryset.product
        instancesold.issue_quantity=queryset.issue_quantity
        # instancesold.issue_quantity=request.user
        #
        messages.success(request, "ISSUED SUCCESSFULLY----------" + "     " + str(instance.quantity) + "  " + str(instance.product) + " products now left in Store")
        
        instancesold.save()
        instance.save()
        return render(request,'stock/stock_detail.html',{'querysetsold':querysetsold,'queryset':queryset})
        # return render(request,'stock/trial.html',{'queryset':instancesold.customer_model})
    context = {
        "title": 'Issue ' + str(queryset.product),
        "queryset": querysetsold,
        "quantity":queryset.quantity,
        "form": formSold,
        "username": 'Issue By: ' + str(request.user),
    }
    return render(request, 'stock/add_item.html', context)

@login_required
def stock_detail(request, stock_pk):
    queryset = Stock.objects.get(id=stock_pk, user=request.user)
    context = {
        "title": queryset.product,
        "queryset": queryset,
    }
    return render(request, 'stock/stock_detail.html', context)

@login_required
def add_items(request):
    form = StockCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        "form": form,
        "title": "Add Item",
    }
    return render(request, 'stock/add_item.html', context)

@login_required
def reorder_level(request, stock_pk):
    queryset = Stock.objects.get(id=stock_pk)
    form = ReorderLevelForm(request.POST or None, instance=queryset)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Reorder level for " + str(instance.product) + " is updated to " + str(instance.reorder_level))
        return redirect('stocklist')
    context = {
            "instance": queryset,
            "form": form,
        }
    return render(request, 'stock/add_item.html', context)

@login_required
def selling_history(request):
    querysetsold = Sold.objects.all()
    return render(request, 'stock/selling_history.html', {'querysetsold':querysetsold})

@login_required
def deletecustomer(request, sold_pk):
    sold = get_object_or_404(Sold, pk=sold_pk)
    if request.method == 'POST':
        sold.delete()
        return redirect('selling_history')
    return render(request, 'stock/delete_customer.html')
