from django.db import models

from shop.models import ProductModel
from users.models import UsersModel


class OrderHistoryModel(models.Model):
    user = models.ForeignKey(UsersModel, on_delete=models.CASCADE, null=True)
    products = models.ManyToManyField(ProductModel)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'order'
        verbose_name_plural = 'orders'
