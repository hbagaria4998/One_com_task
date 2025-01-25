
from django.urls import path
from . import views


urlpatterns = [
    path('', views.ShowProduct,name = "ShowProduct" ),
    path("create_order",views.CreateOrder,name = "CreateOrder")
]