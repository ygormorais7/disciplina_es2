import unittest
from cart import ShoppingCart

class TestRemoveItem(unittest.TestCase):
    def setUp(self):
        self.cart = ShoppingCart()
        self.cart.add_item("Book", 2, 10.0)
        self.cart.add_item("Pen", 5, 1.0)

    def test_remove_item(self):
        self.cart.remove_item("Book")
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.items[0]["name"], "Pen")
        self.assertEqual(self.cart.total, 5.0)

    def test_remove_nonexistent_item(self):
        self.cart.remove_item("Notebook")
        self.assertEqual(len(self.cart.items), 2)
        self.assertEqual(self.cart.total, 25.0)

if __name__ == "__main__":
    unittest.main()