def any_lowercase1(s):
     for c in s:
          if c.islower():
              print('It\'s lower case')
              return True
          else:
              print('It\'s not lower case')
              return False


#any_lowercase1('Lo')


def any_lowercase2(s):
     for c in s:
          if 'C'.islower():
               print('It\'s lower case')
               return 'True'
          else:
               print('It\'s not lower case')
               return 'False'

            
#any_lowercase2('Hello World')


def any_lowercase3(s):
     for c in s:
          flag = c.islower()
          print(flag)
     print(flag)
     return flag

    
    
#any_lowercase3('Hello World')

def any_lowercase4(s):
     flag = False
     for c in s:
          #flag = flag or c.islower()
          flag = flag or c.islower()
     print(flag)
     return flag

#any_lowercase4('HELLsO')


def any_lowercase5(s):
     for c in s:
          if not c.islower():
               print('It\'s not lower case')
               return False
     print('It\'s lower case')
     return True


#print(("ello worlD!").islower())
any_lowercase3('HELLsO')

def for_string(s):
    if s.islower():
        print('it is lower')
    else:
        print('it is not lower')
#for_string('LelLo')



