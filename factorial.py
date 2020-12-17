def factorial(n):
    space = ' ' * (4 * n)
    print (space, 'factorial', n)
    if n == 0:
        print (space, 'returning 1')
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        print (space, 'returning', result)
        return result
factorial(5)


def b(z):
    prod = a(z, z)
    print (z, prod)
    return prod

def a(x, y):
    x = x + 1
    return x * y
def c(x, y, z):
    total = x + y + z
    square = b(total)**2
    return square

x = 1
y = x + 1
print(c(x, y+3, x+y))

def test_function( length, width, height):
    print ("the area of the box is ", length*width*height)
    return length*width*height

l = 12.5
w = 5
h = 2
test_function(l, w, h)

print ("The area of the box is ", length*width*height)
