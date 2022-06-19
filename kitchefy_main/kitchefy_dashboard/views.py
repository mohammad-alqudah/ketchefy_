from django.shortcuts import render

# Create your views here.

def index(request):
     context = {}
     return render(request, 'kitchefy_dashboard/index.html', context)

def kitchefy_portal_finance(request):
     context = {}
     return render(request, "kitchefy_dashboard/kitchefy_portal_finance.html", context)
