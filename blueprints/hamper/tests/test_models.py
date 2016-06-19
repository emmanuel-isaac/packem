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
        models.Hamper.objects.create(name='Valentine special', description='Something for loved ones',)

    def test_hamper_creation(self):
        hamper = models.Hamper.objects.get(name='Valentine special')
        self.assertTrue(isinstance(hamper, models.Hamper))
        self.assertTrue(hamper.__str__(), 'Valentine special')


class ItemHamperLineTestCase(TestCase):
    def setUp(self):
        category = models.Category.objects.create(name="breakables", description="These items can break")
        hamper = models.Hamper.objects.create(name='Valentine special', description='Something for loved ones')
        item = models.Item.objects.create(name='some gift', description='foo-bar', cost=189.382, category=category)
        models.ItemHamperLine.objects.create(item=item, hamper=hamper, item_quantity=5)

    def test_item_hamper_join_creation(self):
        item_hamper = models.ItemHamperLine.objects.get(item__name='some gift', hamper__name='Valentine special')
        self.assertTrue(isinstance(item_hamper, models.ItemHamperLine))
        self.assertTrue(isinstance(item_hamper.item, models.Item))
        self.assertTrue(isinstance(item_hamper.hamper, models.Hamper))
        self.assertTrue(type(item_hamper), int)

    def test_hamper_items(self):
        hamper = models.Hamper.objects.get(name="Valentine special")
        hamper_items = hamper.items.all()
        self.assertTrue(type(hamper_items), list)
        self.assertTrue(len(hamper_items), 1)
        self.assertTrue(isinstance(hamper_items[0], models.Item))

    def test_items_and_their_hamper(self):
        item = models.Item.objects.get(name='some gift')
        items_hampers = item.hamper_set.all()
        self.assertTrue(type(items_hampers), list)
        self.assertTrue(len(items_hampers), 1)
        self.assertTrue(isinstance(items_hampers[0], models.Hamper))
