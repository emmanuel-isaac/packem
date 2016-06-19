from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'categories'

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
    items = models.ManyToManyField(Item, through='ItemHamperLine')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}".format(self.name)


class ItemHamperLine(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    hamper = models.ForeignKey(Hamper, on_delete=models.CASCADE)
    item_quantity = models.IntegerField(null=True, default=1)

    class Meta:
        unique_together = ('item', 'hamper',)
