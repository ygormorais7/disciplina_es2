import unittest
from cart import ShoppingCart

class TestCouponService(unittest.TestCase):
    def setUp(self):
        self.cart = ShoppingCart()
        self.cart.add_item("Book", 2, 10.0)
        self.cart.add_item("Pen", 5, 1.0)

    def test_apply_valid_percent_coupon(self):
        self.cart.apply_coupon("DISCOUNT10")
        total = self.cart.get_total()
        self.assertEqual(total, 22.5)

    def test_apply_valid_fixed_coupon(self):
        self.cart.apply_coupon("DISCOUNT20")
        total = self.cart.get_total()
        self.assertEqual(total, 5.0)

    def test_apply_invalid_coupon(self):
        with self.assertRaises(ValueError):
            self.cart.apply_coupon("INVALID")

if __name__ == "__main__":
    unittest.main()