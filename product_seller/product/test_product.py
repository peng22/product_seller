from django.test import TestCase
from rest_framework.test import APIClient
from product.models import Product
from django.contrib.auth import get_user_model
from .models import Product

#test case example
class productApiTestCase(TestCase):
    def setUp(self):
        self.u1 = get_user_model().objects.create_user(
            username="test1", password="password1"
        )

        self.u2 = get_user_model().objects.create_user(
            username="test2", password="password2"
        )

        products = [
            Product.objects.create(
                seller=self.u1,
                name="product 1 Title",
                price=220,

            ),
            Product.objects.create(
                seller=self.u1,
                name="product 2 Title",
                price=110,

            ),
            Product.objects.create(
                seller=self.u2,
                name="product 3 Title",
                price=330,
                ),

        ]

        # let us look up the product info by ID
        self.product_lookup = {p.id: p for p in products}
        self.client = APIClient()
        # override test client

    def test_product_list(self):
        resp = self.client.get("/api/v1/products/" )
        data = resp.json()
        self.assertEqual(len(data), 3)
        for product_dict in data:
            product_obj = self.product_lookup[product_dict["id"]]
            self.assertEqual(product_obj.name, product_dict["name"])
            self.assertEqual(product_obj.price, product_dict["price"])
            self.assertEqual(product_obj.seller.id, product_dict["seller"])
