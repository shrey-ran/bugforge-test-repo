
def calculate_discount(price, discount_percentage):
    # BUG 1: The math is wrong here. It should be price - (price * (discount_percentage / 100))
    discount_amount = price * (discount_percentage / 100)
    final_price = price + discount_amount 
    return final_price

def get_user_greeting(name):
    # BUG 2: String formatting is incorrect. It should use an f-string or .format().
    return "Hello, {name}! Welcome to the store."

def check_even_number(num):
    # BUG 3: Condition is backwards. Even numbers should have 0 remainder.
    if num % 2 != 0:
        return True
    else:
        return False
