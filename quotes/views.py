from django.shortcuts import render,redirect
from .models import Stock
from django.contrib import messages
from .forms import StockForm
from django.http import HttpResponseRedirect

# Create your views here.
"""1. connect to api
2. grab dara
parse data
do something"""


# iex cloud api : pk_11c5a25bee75409686f4b0316d7c6146


def home(request):
    import requests
    import json


    if request.method == 'POST':
        ticker = request.POST['ticker_symbol']
        api_request = requests.get("https://cloud.iexapis.com/stable/stock/"+ticker+"/quote?token=pk_11c5a25bee75409686f4b0316d7c6146")

        try:
            api = json.loads(api_request.content)  # json parsed into python

        except Exception as e:
            api = "Error..."

        return render(request, 'home.html', {'api': api})

    else:
        return render(request,'home.html', {'ticker':'Enter a Ticker Symbol Above...'})


def about(request):
    return render(request,'about.html',{})

def add_stock(request):
    import requests
    import json

    if request.method == 'POST':
        form = StockForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request,("Stock Has been added.."))
            return redirect('add_stock')
    else:
        ticker_sym = Stock.objects.all()
        output = []
        for ticker_item in ticker_sym:
            api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + str(ticker_item)   + "/quote?token=pk_11c5a25bee75409686f4b0316d7c6146")

            try:
                api = json.loads(api_request.content)  # json parsed into python
                output.append(api)

            except Exception as e:
                api = "Error..."

        return render(request,'add_Stock.html',{'ticker':ticker_sym,'output':output})

def delete(request,id):
    item = Stock.objects.get(pk=id)
    item.delete()
    messages.success(request,("Stock has been deleted.."))
    return redirect(delete_stock)

def delete_stock(request):
    ticker = Stock.objects.all()
    return render(request,'delete_stock.html',{'ticker':ticker})

