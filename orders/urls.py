from django.urls import path

from orders.views import OrderHistoryView, CheckoutView

app_name = 'orders'
urlpatterns = [
    path('order_history/', OrderHistoryView.as_view(), name='order_history'),
    path('checkout/', CheckoutView.as_view(), name='checkout')
]