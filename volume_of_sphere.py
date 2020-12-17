import math

# Calculate the volume of a sphere
def volume_of_sphere(r):
    print('returns a float 0.0')
    return 0.0
# Call to check function initial works
volume_of_sphere(2)


# Calculate the volume of a sphere
def volume_of_sphere(r):
    # calculate cubed of radius r
    r3 = r ** 3
    print('Sphere Radius cubed is ' + str(r3))
    return 0.0
# Call to check function initial works
volume_of_sphere(2)

# Calculate the volume of a sphere
def volume_of_sphere(r):
    # calculate cubed of radius r
    r3 = r ** 3
    # calculate pi(π)
    pi = math.pi
    print('π is ' + str(pi))
    return 0.0
# Call to check function initial works
volume_of_sphere(2)

# Calculate the volume of a sphere
def volume_of_sphere(r):
    # calculate cubed of radius r
    r3 = r ** 3
    # calculate pi(π)
    pi = math.pi
    # volume of sphere
    v = (4/3) * pi * r3
    print('Volume of sphere is ' + str(v))
    return v
# Call to check function initial works

volume_of_sphere(4)
