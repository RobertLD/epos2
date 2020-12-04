from django.test import TestCase
from shop.models import Product, Category 
from django.contrib.auth.models import Group, User
class AnimalTestCase(TestCase):
    def setUp(self):
        z = Category.objects.create(name="Appetizer")
        Product.objects.create(name= "Banana", Category=z, price = 1, stock = 1, slug = "Dfdfd")
        Product.objects.create(name= "Apple", Category=z, price = 1, stock = 1,slug = "Dfdfdsdf3e")

    def test_product_category_creation(self):
        lion = Product.objects.get(name="Banana")
        self.assertEqual(lion.name, "Banana")
        self.assertEqual(lion.Category.name, "Appetizer")

    def test_product_category_search_nonexist(self):
        try:
            a = Product.objects.get(name="Apples")
        except Product.DoesNotExist as e:
            return True

    def test_user_create(self):
        try:
            User.objects.create(username="billy", password = "ugly")
            a = User.objects.get(username="billy")
            if (not a.DoesNotExist):
                return True
            else:
                return False   
        except e:
            return False
        
        

        