from django.urls import path

from shop.views import ShopView

app_name = 'shop'
urlpatterns = [
        path('', ShopView.as_view(), name='shop')
]