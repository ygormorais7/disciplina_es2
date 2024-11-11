import unittest
from cart import ShoppingCart

class TestAddItem(unittest.TestCase):
    def setUp(self):
        self.cart = ShoppingCart()

    def test_add_item(self):
        self.cart.add_item("Book", 2, 10.0)
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.items[0]["name"], "Book")
        self.assertEqual(self.cart.items[0]["quantity"], 2)
        self.assertEqual(self.cart.items[0]["price"], 10.0)
        self.assertEqual(self.cart.total, 20.0)

if __name__ == "__main__":
    unittest.main()