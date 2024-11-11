import unittest
from cart import ShoppingCart

class TestCalculateTotal(unittest.TestCase):
    def setUp(self):
        self.cart = ShoppingCart()
        self.cart.add_item("Book", 2, 10.0)
        self.cart.add_item("Pen", 5, 1.0)

    def test_get_total(self):
        total = self.cart.get_total()
        self.assertEqual(total, 25.0)

if __name__ == "__main__":
    unittest.main()