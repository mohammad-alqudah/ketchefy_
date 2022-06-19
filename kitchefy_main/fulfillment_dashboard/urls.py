
from django.urls import path

from . import views

urlpatterns = [
        #Leave as empty string for base url
	path('', views.index, name="index"),
	path('incidents_reports_hub', views.incidents_reports_hub, name="incidents_reports_hub"),
	path('inventory_sales_forecast', views.inventory_sales_forecast, name="inventory_sales_forecast"),
	path('knowledge_center', views.knowledge_center, name="knowledge_center"),
	path('orders_details', views.orders_details, name="orders_details"),

]