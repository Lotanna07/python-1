#if/else

customer_age =17
is_student = True

if customer_age < 18:
    print("You are a minor.")
elif customer_age >= 18 and customer_age < 65:
    print("You are an adult.")
else:
    print("Everyone pays full price.")