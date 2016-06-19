from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return "{}".format(self.name)


class Item(models.Model):
    name = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    category = models.ForeignKey(Category)
    cost = models.FloatField()

    def __str__(self):
        return "{}".format(self.name)


class Hamper(models.Model):
    name = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=255, null=True)

    def __str__(self):
        return "{}".format(self.name)


class ItemHamper(models.Model):
    item = models.ForeignKey(Item, null=True)
    hamper = models.ForeignKey(Hamper, null=True)
    item_quantity = models.IntegerField(null=True)
