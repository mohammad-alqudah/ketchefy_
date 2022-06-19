from django.shortcuts import render

# Create your views here.

def index(request):
     context = {}
     return render(request, 'fulfillment_dashboard/index.html', context)

def incidents_reports_hub(request):
     context = {}
     return render(request, 'fulfillment_dashboard/incidents&reports_hub.html', context)

def inventory_sales_forecast(request):
     context = {}
     return render(request, 'fulfillment_dashboard/inventory&sales_forecast.html', context)

def knowledge_center(request):
     context = {}
     return render(request, 'fulfillment_dashboard/knowledge_center.html', context)

def orders_details(request):
     context = {}
     return render(request, 'fulfillment_dashboard/orders_details.html', context)

