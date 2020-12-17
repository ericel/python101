# Define a function that takes an argument. Call the function. Identify what code is the argument and what code is the parameter.
def sentence(st):
    # Convert the arguement to a string parameter.
    convertedToString = str(st)
    
    # Get parameter length
    strLength = len(convertedToString)
    
    # Check if parameter(converted string) already ends with the puntuation period.
    # If no, then add period at end of sentence.
    if convertedToString.endswith('.'):
        correctSentence = convertedToString.capitalize()
    else:
        correctSentence = convertedToString.capitalize() + '.'
        
    # Finally print our not perfect grammar sentence.
    print(correctSentence)

    
# Call your function from Example 1 three times with different kinds of arguments: a value, a variable, and an expression.
# Identify which kind of argument is which.

# Call sentence function with value
sentence("today weather is so cold")

# Call sentence function with variable
dressing = "You should dress properly with a coat, scarf, socks, and boots."
sentence(dressing)

# Call sentence with an expression
otherwise = "If not,"
sentence(otherwise +  "you risk getting sick sooner!")

# Create a function with a local variable. Show what happens when you try to use that variable outside the function.
# Explain the results.
def onlyLocalVariable():
    _local = "I exist only within these walls"
    print(_local)

#print(_local
#Traceback (most recent call last):
#  File "/Users/ericel123/Documents/UoPeople/python 101/discussion2.py", line 39, in <module>
#    print(_local)
#NameError: name '_local' is not defined

# Create a function that takes an argument. Give the function parameter a unique name.
# Show what happens when you try to use that parameter name outside the function. Explain the results.

def uniquParameter(uopeople):
    print(uopeople)

#print(uopeople)
#Traceback (most recent call last):
#  File "/Users/ericel123/Documents/UoPeople/python 101/discussion2.py", line 52, in <module>
#    print(uopeople)
#NameError: name 'uopeople' is not defined


# Show what happens when a variable defined outside a function has the same name as a local variable inside a function.
# Explain what happens to the value of each variable as the program runs.

_global = 4

def sameGlobalLocalVariable():
    #_global = 3
    print(_global)

print(_global)
sameGlobalLocalVariable()
print(_global)
#4
#3

def func(james):  # James = parameter

    print("Hi james") #Hi James = the argument

    return message;
func('hi James')
