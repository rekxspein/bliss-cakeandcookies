from django.db import models
from django.contrib.auth.models import User
from products.models import Product

from users.models import UserAddress

from .utils import unique_order_id_generator
from django.db.models.signals import pre_save

# order model

ORDER_STATUS_CHOICES = (
    ('Not Yet Shipped', 'Not Yet Shipped'),
    ('Shipped', 'Shipped'),
    ('Cancelled', 'Cancelled'),
    ('Refunded', 'Refunded'),
)


class Order(models.Model):
    order_id = models.CharField(max_length=100, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=120, default='Not Yet Shipped', choices=ORDER_STATUS_CHOICES)
    total_amount = models.IntegerField(default=0, null=False, blank=False)
    address = models.ForeignKey(UserAddress, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username + " " + self.order_id

    @staticmethod
    def get_all_orders():
        return Order.objects.all()


def pre_save_create_order_id(sender, instance, *args, **kwargs):
    if not instance.order_id:
        instance.order_id = unique_order_id_generator(instance)


pre_save.connect(pre_save_create_order_id, sender=Order)


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, related_name="orders_item", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField(default=0)
    item_total = models.IntegerField(default=0)

    def __str__(self):
        return self.product.name + " " + self.order.order_id
