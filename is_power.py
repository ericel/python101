# Checks if x is divisible by y.
def is_divisible(x, y):
    if x % y == 0:
        return True
    else:
        return False


# Checks if x is power of y
def is_power(x, y):
    # x must be greater than or equal to y
    # x,y should be positive integers but y could be zero as 0 ** 0 = 1
    # where 1, is a possibility of zero to power zero
    if x < 1: 
        return False
    
    # base case of the second argument(y) being "1"
    elif y == 1 and x > 1:
        return False
    
    # In case two arguments being equal
    # Y ** 0 = 1, e.g 3 ** 0 = 1. so true
    elif x == y or x == 1: 
        return True
    
    else:
        # is_power function call is_divisible
        # is_power function call itself recursively
        return is_divisible(x,y) and is_power(x/y, y)


print("is_power(10, 2) returns: ", is_power(10, 2))
print("is_power(27, 3) returns: ", is_power(27, 3))
print("is_power(1, 1) returns: ", is_power(1, 1))
print("is_power(10, 1) returns: ", is_power(10, 1))
print("is_power(3, 3) returns: ", is_power(3, 3))
