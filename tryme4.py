# prints a new line on each call
# Each new line is denoted by a period(.)
def new_line():
    print('.')

# prints a total of 3 lines on each call
def three_lines():

    new_line()

    new_line()

    new_line()

# prints a total of 9 lines on each call
def nine_lines():
    three_lines()
    three_lines()
    three_lines()


# prints a total of 25 lines on each call
def clear_screen():
    # I use a for loop in the range run nine_lines twice
    for i in range(2):
        nine_lines()
    # I use a for loop in the range run three_lines twice
    for i in range(2):
        three_lines()
    new_line()
    
# Placeholder Printing 9 lines
print("Printing 9 Lines")
# Should print 9 lines
nine_lines()

# Placeholder Printing 25 lines
print("Printing 25 Lines")
# Should print 25 lines
clear_screen()

          
