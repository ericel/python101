import math
# Part 1. Returns an estimate of the square root of a
def my_sqrt(a):
    # initialize x
    # x as estimate of any number. It could be any number.
      x = (a + 5) * 2
      while True:
        y = (x + a/x) / 2
        if y == x:
            return x
        #print(y)
        x = y

# Print a and value
def print_a(a):
    return ('a = ' + str(a))
#print | pipe
def print_posts(a):
    if len(str(a)) > 1:
         return (' | ')
    else:
        return ('  | ')

# Print my_sqrt
def print_my_sqrt(a):
    return ('my_sqrt(a) = ' + str(my_sqrt(a)))

# Print math sqrt
def print_math_sqrt(a):
    return ('math.sqrt(a) = ' + str(math.sqrt(a)))

# Callculate absolute difference between my_sqrt(a) and print_math_sqrt(a)
# Print the diff
def absolute_diff(a):
    diff = abs(my_sqrt(a) - math.sqrt(a))
    return ('diff = ' + str(diff))

    
# Part 2. Prints a table with a while loop
def test_sqrt():
    a = 1
    while a <= 25:
        #print(print_posts())
        print(print_a(a) + print_posts(a) + print_my_sqrt(a) +
              print_posts(a) + print_math_sqrt(a) + print_posts(a) +
              absolute_diff(a)
             )
        a += 1
        
test_sqrt()
