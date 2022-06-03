from django.db import models
from django.contrib.auth.models import User



# User Address Model
class UserAddress(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    postal_code = models.CharField(max_length=10)
    mobile = models.IntegerField()
    customer = models.ForeignKey(
        User, related_name="customer_address", on_delete=models.CASCADE)

    def __str__(self):
        return self.address

