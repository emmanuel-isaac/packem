from django.contrib import admin

from .models import Category, Hamper, Item, ItemHamperLine


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Hamper)
class HamperAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    fields = ('name', 'description',)


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass


@admin.register(ItemHamperLine)
class ItemHamperAdmin(admin.ModelAdmin):
    list_display = ('hamper', 'item', 'item_quantity')
