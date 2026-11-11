#function

def apply_discount(price, percent):
    discount_amount = price * (percent / 100)
    new_price = price - discount_amount
    return new_price

new_price = apply_discount(1000, percent=10)
print(new_price)