from django.shortcuts import render

# Create your views here.

def index(request):
     context = {}
     return render(request, 'kitchefy_dashboard/index.html', context)

def kitchefy_portal_finance(request):
     context = {}
     return render(request, "kitchefy_dashboard/kitchefy_portal_finance.html", context)

def knowledge_center(request):
     context = {}
     return render(request, "kitchefy_dashboard/knowledge_center.html", context)

def inventory_sales_forecast(request):
     context = {}
     return render(request, "kitchefy_dashboard/inventory_sales_forecast.html", context)

def orders_details(request):
     context = {}
     return render(request, "kitchefy_dashboard/orders_details.html", context)

def inceidents_ratings_hub(request):
     context = {}
     return render(request, "kitchefy_dashboard/inceidents_ratings_hub.html", context)



