# Return inverted dictionary
def invert_dict(d):
     inverse = dict()
     # Loop through items in original dict
     # To get each key list values
     for key in d:
         
          # Loop through items in dict list values
          for item in d[key]:
              
              # Check for key in inverted list
              if item not in inverse:
                   inverse[item] = [key]
                   
              # If key doesn't exist
              # Add new key list value
              else:
                   inverse[item].append(key)
                   
     # Print / return inverted dict with each
     # list items turned into separate keys
     #print('Inverted dictionary ' + str(inverse))
     return inverse

import ast

# open Our original_dict.txt input file
try:
    users = open('original_dict.txt', 'r')

    # Convert back to dict using ast module
    dict_users = ast.literal_eval(users.read())
    
    # print Original Dictionary
    print('Original dictionary ' + str(dict_users))
    users.close()
    print('\n****************PlaceHolder*************\n')
    
    # Invert the original Dictionary
    invert_dict(dict_users)
    print('Inverted dictionary ' + str(invert_dict(dict_users)))

    # Write to inverted_output.txt file
    inverted_output = open("inverted_output.txt","w")
    
    # Convert dictionary to string before writing to file
    # Only strngs can be written to file
    inverted_output.write(str(invert_dict(dict_users)))
    inverted_output.close()

  
except Exception as err:
    print(type(err))    # the exception type
    print(err.args)     # exception arguments as tuples
    print(err.args[1])  # better error message 
    print(err)   

