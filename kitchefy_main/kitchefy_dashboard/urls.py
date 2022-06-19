
from django.urls import path

from . import views

urlpatterns = [
        #Leave as empty string for base url
	path('', views.index, name="index"),
        path('kitchefy_portal_finance', views.kitchefy_portal_finance,name="kitchefy_portal_finance")

]