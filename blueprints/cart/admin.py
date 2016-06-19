from django.contrib import admin

from models import Cart, CartItemLine, CartHamperLine


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    pass


@admin.register(CartItemLine)
class CartItemLineAdmin(admin.ModelAdmin):
    pass


@admin.register(CartHamperLine)
class CartHamperLineAdmin(admin.ModelAdmin):
    pass
