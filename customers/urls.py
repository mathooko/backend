from django.urls import path
from .views import CustomerListView

urlpatterns=[
    path("signup/",CustomerListView.as_view(), name="customer_signup"),
    
    
]