# Counts down to 0 positive intergers
def countdown(n):
     if n <= 0:
          print('Blastoff!')
     else:
          print(n)
          countdown(n-1)

# Counts up to 0 negative intergers
def countup(n):
     if n >= 0:
          print('Blastoff!')
     else:
          print(n)
          countup(n+1)

# Take input as positive or negative number or zero
user_input = input("Please enter a lucky number..")

# Let's run countdown() for positive Intergers
# And run countup() for negative intergers
# For zeros, let's countup in a nested function
def number_counts():
    num_input = int(user_input)
    if num_input > 0:
        countdown(num_input)
    elif num_input == 0:
        countup(num_input)
    else:
        countup(num_input)
       
# On user input countdown, countup
number_counts()







