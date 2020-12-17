
# transforms first letter to uppercase
def to_uppercase(month):
    return month.capitalize()

# Transforms list to list uppercase
def wintermonths_uppercase(months):
    # Apply to_uppercase to every item of our list argument
    months = map(to_uppercase, months)

    wintermonths = list(months)

    print(wintermonths)

    # Use referecing to assign our list object to coldmonths
    coldmonths = wintermonths

    print(coldmonths)

    # Mutability check on our object references
    coldmonths[0] = 'October'

    print(coldmonths)
    print(wintermonths)

    

wintermonths_uppercase(['november', 'december', 'january', 'february'])



