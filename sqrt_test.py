Import math

# my_sqrt function which takes single argument and also includes while loop.

 

def my_sqrt (a) :  #this takes a parameter a

X = a/2                   #initialize x

While True:

       y = (x + a/x) / 2.0

       If y == x :

           return y

          break

x = y           #returns  x  final value

 

def  test_sqrt () :

       n  =  1

     while n <=25:     #modified  from 9 to 25

            print ("a =",  n,  "| my_sqrt (a)  =",  my_sqrt (n),   "|  math_sqrt (a)  =",

math.sqrt (n),  "|  diff =",  abs(my_sqrt(n)   -  math.sqrt(n) ) )

               n = n + 1

               # ("a = ",  n,  "                                                         First column prints

the number  'a '

               #|  my_sqrt(a)    =",  my_sqrt(n)  ,  "                  Second column prints

the square root of  'a'   computed with my_sqrt

               #|  math_sqrt (a)   =",  math.sqrt (n), "              Third column prints

the square root of 'a'  computed by the math.sqrt

                #| diff  =",   abs (my_sqrt (n)  - math.sqrt (n) ) ) Fourth column prints

the difference between the two  in absolute value

 

test_sqrt ()

 
