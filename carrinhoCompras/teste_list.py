import unittest
from cart import ShoppingCart

class TestListItems(unittest.TestCase):
    def setUp(self):
        self.cart = ShoppingCart()
        self.cart.add_item("Book", 2, 10.0)
        self.cart.add_item("Pen", 5, 1.0)

    def test_list_items(self):
        items = self.cart.get_items()
        self.assertEqual(len(items), 2)
        self.assertEqual(items[0]["name"], "Book")
        self.assertEqual(items[0]["quantity"], 2)
        self.assertEqual(items[0]["price"], 10.0)
        self.assertEqual(items[1]["name"], "Pen")
        self.assertEqual(items[1]["quantity"], 5)
        self.assertEqual(items[1]["price"], 1.0)

if __name__ == "__main__":
    unittest.main()