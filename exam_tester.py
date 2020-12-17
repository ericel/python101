
pi = float(3.14159)
print (pi)


for fruit in ["banana", "apple", "quince"]:
    print (fruit)

n = 1000
count = 0
while n:
    count = count + 1
    n = n // 10
print (count)

index = "Ability is a poor man's wealth".find("w")
print(index)

i = 2
def myf(s, n):

    global i

    print(s * i * n)

myf('hi-', 3)


try:
    fin = open('the_file', 'r')
except:
    fin = open('the_file', 'w')
fin.close()

my_list = [3, 2, 1]
print(my_list)



n = 10
while n != 1:
    print (n,)
    if n % 2 == 0: # n is even
        n = n // 2
    else: # n is odd
        n = n * 3 + 1

mylist = [ [2,2,1], [1,2,3], [1,1,1] ]
total = 0
for sublist in mylist:
    total += sum(sublist)
print(total)

def recurse(a):
    if (a == 0):
        print(a)
    else:
        recurse(a) 

recurse(0)

def area(l, w):
    temp = l * w;
    return temp

l = 4.0
w = 3.25
x = area(l, w)
if ( x ):
  print (x)
