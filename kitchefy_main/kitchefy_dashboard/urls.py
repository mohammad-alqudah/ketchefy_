
from django.urls import path

from . import views

urlpatterns = [
        #Leave as empty string for base url
	path('', views.index, name="kitchefy_index"),
    path('portal_finance', views.kitchefy_portal_finance,name="portal_finance"),
	path('knowledge_center', views.knowledge_center, name="kitchefy_knowledge_center"),
	path('inceidents_ratings_hub', views.inceidents_ratings_hub, name="kitchefy_inceidents_ratings_hub"),
	path('orders_details', views.orders_details, name="kitchefy_orders_details"),
	path('inventory_sales_forecast', views.inventory_sales_forecast, name="kitchefy_inventory_sales_forecast"),

]
