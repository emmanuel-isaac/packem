from django.test import TestCase

from ..models import Cart, CartHamperLine, CartItemLine
from blueprints.hamper.models import Item, Category, Hamper
from blueprints.user.models import User


class CartTestCase(TestCase):
    def setUp(self):
        category = Category.objects.create(name="breakables", description="These items can break")
        self.item = Item.objects.create(name='some gift', description='foo-bar', cost=189.382, category=category)
        self.hamper = Hamper.objects.create(name='Valentine special', description='Something for loved ones',)
        self.hamper_2 = Hamper.objects.create(name='MalcomX', description='Sweet Something',)
        self.user = User.objects.create(email='foo@bar.com', first_name='foo', last_name='bar', password='fooBar')
        self.cart = Cart.objects.create(user=self.user,)

    def test_creation(self):
        self.cart = Cart.objects.last()
        self.assertTrue(isinstance(self.cart, Cart))

    def test_add_item_to_cart(self):
        CartItemLine.objects.create(cart=self.cart, item=self.item)
        cart_items = self.cart.items.all()
        self.assertEqual(len(cart_items), 1)
        self.assertTrue(isinstance(cart_items[0], Item))

    def test_add_hamper_to_cart(self):
        CartHamperLine.objects.create(cart=self.cart, hamper=self.hamper)
        CartHamperLine.objects.create(cart=self.cart, hamper=self.hamper_2)
        cart_hampers = self.cart.hampers.all()
        self.assertEqual(len(cart_hampers), 2)
        self.assertTrue(isinstance(cart_hampers[0], Hamper))
