  
test_dups = ["zzz","dog","bookkeeper","subdermatoglyphic","subdermatoglyphics"] 

alphabet = "abcdefghijklmnopqrstuvwxyz"

test_miss = ["zzz","subdermatoglyphic","the quick brown fox jumps over the lazy dog"] 

def histogram(s):
     d = dict()
     for c in s:
          if c not in d:
               d[c] = 1
          else:
               d[c] += 1
     return d

#part 1
# Check is string character has duplicates
def has_duplicates(s):
    # histogram dictionary 
    init_dict = histogram(s)
      
    # using for loop to 
    # check for duplicate values count > 1 
    flag = False
    for c in init_dict:
        if init_dict[c] > 1:
            #print('Duplicates Found')
            flag = True
            break
        else : 
            #print('No Duplicates')
            flag = False
      
    # print result of flag
    return flag
#has_duplicates('helkmgo')

# Loop to checks if string has duplicates and prints string
for s in test_dups:
    if has_duplicates(s):
        print(s + ' has duplicates')
    else:
        print(s + ' has no duplicates')


#>>>
#zzz has duplicates
#dog has no duplicates
#bookkeeper has duplicates
#subdermatoglyphic has no duplicates
#subdermatoglyphics has duplicates

# Print placeholder between part 1 and part 2
print('\n-------------------------------------------------------------\n')


#part 2
#returns alphabet letters not in the string
def missing_letters(s):
    # Initialize not_in_string_list
    not_in_string_list = []
    
    # Initialize alphabet histogram dict
    alphabet_dict = histogram(alphabet)
    
    for c in alphabet_dict:
        if c not in s:
            not_in_string_list.append(c)
        else:
            not_in_string_list
            
    # Print sorted results
    sortedList = sorted(not_in_string_list)
    
    # Convert list to string
    delimiter = ''
    stringNot = delimiter.join(sortedList)

    # Return string alphabets characters not in string
    return stringNot


# Loop to Check and print missing alphabet characters
for s in test_miss:
    missingString = missing_letters(s)
    if len(missingString) > 0:
        print(s + ' is missing letters ' + missingString)
    else:
        print( s + ' uses all the letters') 
            
#check_print_test_miss()
#zzz is missing letters abcdefghijklmnopqrstuvwxy
#subdermatoglyphic is missing letters fjknqvwxz
#the quick brown fox jumps over the lazy dog uses all the letters
