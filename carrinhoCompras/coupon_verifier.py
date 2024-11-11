class CouponService:
    def __init__(self):
        self.valid_coupons = {
            "DISCOUNT10": {"type": "percent", "amount": 10},
            "DISCOUNT20": {"type": "fixed", "amount": 20},
            "DISCOUNT5": {"type": "percent", "amount": 5}
        }

    def validate_coupon(self, coupon_name):
        return coupon_name in self.valid_coupons
    
    def get_type(self, coupon_name):
        return self.valid_coupons[coupon_name]["type"]
    
    def get_amount(self, coupon_name):
        return self.valid_coupons[coupon_name]["amount"]