# kitchen.py (อัปเดตให้เป็นแบบนี้)
class Quantity:
    def __init__(self, amount):
        self.amount = amount

    def times(self, multiplier):
        return Quantity(self.amount * multiplier)

    # เพิ่ม 2 เมทอดนี้เข้ามา
    def __eq__(self, other):
        return self.amount == other.amount

    def __repr__(self):
        return f"Quantity({self.amount})"