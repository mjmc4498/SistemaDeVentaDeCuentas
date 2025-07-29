from django.urls import path
from . import views

app_name = 'payments'

urlpatterns = [
    path('', views.bill_list, name='bill_list'),
    path('pay/<int:bill_id>/', views.pay_bill, name='pay_bill'),
]
