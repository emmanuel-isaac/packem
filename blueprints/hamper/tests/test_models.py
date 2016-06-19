from django.test import TestCase

from blueprints.hamper import models


class CategoryTestCase(TestCase):
    def setUp(self):
        self.category = models.Category.objects.create(name="breakables", description="These items can break")

    def test_category_creation(self):
        self.assertTrue(isinstance(self.category, models.Category))
        self.assertTrue(self.category.__str__(), 'breakables')


class ItemTestCase(TestCase):
    def setUp(self):
        category = models.Category.objects.create(name="breakables", description="These items can break")
        models.Item.objects.create(name='some gift', description='foo-bar', cost=189.382, category=category)

    def test_item_creation(self):
        item = models.Item.objects.get(name='some gift')
        self.assertTrue(isinstance(item, models.Item))
        self.assertTrue(item.__str__(), 'some gift')
        self.assertTrue(isinstance(item.category, models.Category))
        self.assertTrue(type(item.cost), float)


class HamperTestCase(TestCase):
    def setUp(self):
        models.Hamper.objects.create(name='Valentine special', description='Something for loved ones')

    def test_hamper_creation(self):
        hamper = models.Hamper.objects.get(name='Valentine special')
        self.assertTrue(isinstance(hamper, models.Hamper))
        self.assertTrue(hamper.__str__(), 'Valentine special')


class HamperItemJoinTestCase(TestCase):
    def setUp(self):
        category = models.Category.objects.create(name="breakables", description="These items can break")
        hamper = models.Hamper.objects.create(name='Valentine special', description='Something for loved ones')
        item = models.Item.objects.create(name='some gift', description='foo-bar', cost=189.382, category=category)
        models.ItemHamper.objects.create(item=item, hamper=hamper, item_quantity=5)

    def test_item_hamper_join_creation(self):
        item_hamper = models.ItemHamper.objects.get(item__id=1, hamper__id=1)
        self.assertTrue(isinstance(item_hamper, models.ItemHamper))
        self.assertTrue(isinstance(item_hamper.item, models.Item))
        self.assertTrue(isinstance(item_hamper.hamper, models.Hamper))
        self.assertTrue(type(item_hamper), int)
