from coupon_verifier import CouponService

class ShoppingCart():
    def __init__(self):
        self.items = []
        self.total = 0
        self.verifier = CouponService()

    def add_item(self, name, quantity, price):
        item = {
            "name": name,
            "quantity": quantity,
            "price": price
        }
        self.items.append(item)
        self.total += quantity * price

    def remove_item(self, name):
        for item in self.items:
            if item["name"] == name:
                self.total -= item["quantity"] * item["price"]
                self.items.remove(item)
                break
            else:
                raise ValueError("Invalid item") 

    def get_total(self):
        return self.total
    
    def apply_coupon(self, coupon):
        if self.verifier.validate_coupon(coupon):
            type_coupon = self.verifier.get_type(coupon)
            amount_coupon = self.verifier.get_amount(coupon)

            if type_coupon == "percent":
                self.discount = self.total * (amount_coupon / 100)
            elif type_coupon == "fixed":
                self.discount = amount_coupon

        else:
            raise ValueError("Invalid coupon")
        
        self.total -= self.discount

    def get_items(self):
        return self.items