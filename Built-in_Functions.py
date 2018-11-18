#abs(x): Return the absolute value of a number. The argument may be an integer or a floating point number. If the argument is a complex number, its magnitude is returned.
print(abs(-2.14))

#bin(x):Convert an integer number to a binary string prefixed with “0b”. The result is a valid Python expression
print(bin(10))

#chr(i):Return the string representing a character whose Unicode code point is the integer i.
print(chr(97))

#complex([real[,imag]]):Return a complex number with the value real + imag*1j or convert a string or number to a complex number.
print(complex('4+3j'),complex(8,2),complex(0))

#divmod(a,b):Return a pair of numbers consisting of their quotient and remainder when using integer division.
print(divmod(13,5))

#enumerate(iterable,start):
seasons=['Spring','Summer','Autumn','Winter']
print(list(enumerate(seasons)))
print(list(enumerate(seasons,start=1)))

#eval(expression,golbals=None,locals=None):The expression argument is parsed and evaluated as a Python expression
x=1
print(eval('x+2'))

#filter():The filter() method filters the given sequence with the help of a function that tests each element in the sequence to be true or not.


#float(x):
print(float(+1.23),float('     -12345\n'),float('1e-003'),float('+1E6'),float('-Infinity'))

#format():
print("I am {} years old!".format(19))

#frozenset():Returns an immutable frozenset object initialized with elements from the given iterable.
vowels=['a','e','i','o','u']
fix=frozenset(vowels)
print("The frozen set is:",fix)

#getattr():
class Person:
	age=19
	name='Sam'
person=Person()
print('The name is:',getattr(person,'age'))
print('The name is:',person.age) #equivalent to the above statement
print('The sex is:',getattr(person,'sex','Male')) #The value passed is default value incase the attribute is missing

#hex(x):Convert an integer number to a lowercase hexadecimal string prefixed with “0x”.
print(hex(255))

#iter() and next():
vowels = ['a', 'e', 'i', 'o', 'u']
vowelsIter = iter(vowels)
print(next(vowelsIter))
print(next(vowelsIter))
print(next(vowelsIter))

#oct(x):Convert an integer number to an octal string prefixed with “0o”.
print(oct(8))

#ord(x): return an integer representing the Unicode code point of that character.
print(ord('A'))

#setattr(object,name,value):E.g. - setattr(x,'footbar',123) is equivalent to x.footbar=123