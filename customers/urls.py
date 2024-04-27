from django.urls import path
from .views import CustomerListView, CustomerLoginView,LaundryServiceView,SelectedView,OrderEdit

urlpatterns=[
    path("signup/",CustomerListView.as_view(), name="customer_signup"),
    path("login/",CustomerLoginView.as_view(), name= "customer_login"),
    path("services/",LaundryServiceView.as_view(),name="services"),
    path("selected/<user>/",SelectedView.as_view(),name="selected"),
    path("edit/<int:pk>/",OrderEdit.as_view(), name="edit")
]