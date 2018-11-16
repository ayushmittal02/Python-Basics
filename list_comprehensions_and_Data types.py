#Different list comprehensions

squares = []
for x in range(10):
	squares.append(x**2)
print(squares)

squares=list(map(lambda x: x**2,range(10)))
print(squares)

squares=[x**2 for x in range (10)]
print(squares)

l=[(x,y) for x in [1,2,3] for y in [3,1,4] if x!=y]
print(l)

vec=[1,2,3,4]
vec2=[x**2 for x in vec]
print(vec2)

vec3=[x for x in vec if x>2]
print(vec3)

l=[(x,x**2) for x in range (5)]
print(l)

from math import pi 
l=[str(round(pi,i)) for i in range (5)]
print(l)

#TUPLES (They are immutable)

empty=()
singleton='hello',  #Special case - If tuple contains one element. It should end with a comma.
print(len(empty))
print(len(singleton))
print(singleton)

t=12345,54321,'hello'  #tuple packing
print(t)
print(len(t))

x,y,z=t   #sequence unpacking
print(x)
print(y)
print(z)

#SETS

basket={'apple','orange','apple','pear','orange','banana'}
print(basket)  #show that duplicates have removed

print('orange' in basket)  #fast membership testing

#Demonstrate sets operations on unique letters from two words

a=set('abracadabra')
b=set('alacazam')
print(a) #unique letters in a
print(a-b) #letters in a but not in b
print(a|b)  #letters in a or b or both
print(a&b) #letters in both a and b
print(a^b)  #letters in a or b but not both

#DICTIONARY (key:value)

tel={'jack':4098,'sape':4139}
tel['guido']=4127
print(tel)
print(list(tel))

d=dict([('sape',4139),('jack',4098)])  #Using dict() constructor
print(d)

a,b,c=tel.items()  #Retrieve key and value at the same time using items()
print(a,b,c)

#Enumerate() function:

for i,j in enumerate(['tic','tac','toe']):
	print(i,j)

#Zip() function:

questions=['name','quest','favourite colour']
answers=['lancelot','the holy grail','blue']
for a,b in zip(questions,answers):
	print('What is your {0}? It is {1}.'.format(a,b))
