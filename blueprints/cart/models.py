from django.db import models

from blueprints.hamper.models import Hamper, Item
from blueprints.user.models import User


class Cart(models.Model):
    items = models.ManyToManyField(Item, through='CartItemLine')
    hampers = models.ManyToManyField(Hamper, through='CartHamperLine')
    paid_for = models.BooleanField(default=False)
    user = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}'s cart, created {}".format(self.user.username, self.created)


class CartItemLine(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    item_quantity = models.IntegerField(default=1)
    added = models.DateTimeField(auto_now_add=True)


class CartHamperLine(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    hamper = models.ForeignKey(Hamper, on_delete=models.CASCADE)
    hamper_quantity = models.IntegerField(default=1)
    added = models.DateTimeField(auto_now_add=True)
