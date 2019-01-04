"""Customising built-in functions"""
#sorted
print(sorted([1,-2,3]))
print(sorted([1,-2,3], key=abs)) #Sorts values according to their absolute values

#map()
print(list(map(str,[1,2,3])))

def add_2(x):
	x+=2
	return x
print(list(map(add_2,[1,2,3]))) #Passing custom function

#filter(): Compares the iterable with the first parameter and returns the values which are 'True'
print(list(filter(None,[0,2,4])))

def greater_than_10(num):
	return num>10
print(list(filter(greater_than_10,range(1,15))))

#reduce():Returns a single value by evaluating the second parameter according to the first parameter
import functools
import operator
print(functools.reduce(operator.mul,[2,4,5]))

#Decorator
def make_pretty(func):
	def inner():
		print("I got decorated")
		func()
	return inner

def ordinary():
	print("I am Ordinary")
print(ordinary())

ordinary=make_pretty(ordinary)
print(ordinary())

@make_pretty				#Equivalent to above statement
def ordinary():
	print("I am Ordinary")

print(ordinary())