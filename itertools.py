import itertools
import operator
l1=[1,4,5,7]
l2=[1,4,6,8]
l3=[3,6,5,0]
print('The sum after each iteration is:',end='') #prints successive summation of elements.
print(list(itertools.accumulate(l1))) #Using Accumulation

print('The product after each iteration is:',end='')
print(list(itertools.accumulate(l1,operator.mul)))  #prints successive multiplication of elements.

#Chain(): Joins all the elements in the iterables into one.
print("All values in chain are:",end='')
print(list(itertools.chain(l1,l2,l3)))

l4=[l1,l2,l3]
print(list(itertools.chain.from_iterable(l4)))

#Compress(): Selectively prints the elements according to the Boolean list. Only True Boolean values are printed.
print(list(itertools.compress('AyushMittal',[1,0,0,0,1,1,1,0,0,0,0]))) 

#dropwhile():
l=[2,4,5,7,8]
print("The values after condition returns false:", end='')
print(list(itertools.dropwhile(lambda x: x%2==0,l)))

#filterfalse():
print("The values that return false to function are:", end='')
print(list(itertools.filterfalse(lambda x: x%2==0,l)))

#islice():
l=[2,4,5,7,8,10,20]
print("The sliced list values are:", end='')
print(list(itertools.islice(l,1,6,2)))

#starmap():
l=[(1,10,5),(8,4,1),(5,4,9),(11,10,1)]
print("The values acc. to function are:", end='')
print(list(itertools.starmap(min,l)))

#takewhile():
l=[2,4,5,7,8]
print("The values till condition returns false:", end='')
print(list(itertools.takewhile(lambda x:x%2==0,l)))

#zip_longest():
print("The combined values of iterables is:", end='')   #prints the values of iterables alternatively in sequence.
print(*(itertools.zip_longest('GesoGes','ekfrek',fillvalue='_')))

#product():
print("The cartesian product is:", end='')
print(list(itertools.product('AB','12')))

#permutations():
print("All the permutations are:", end='')
print(list(itertools.permutations('gfg',2)))

#combinations():
print("All the combination in sorted order (without replacement):", end='')
print(list(itertools.combinations('1234',2)))

#combinations_with_replacement():
print("All the combination in sorted order (with replacement):", end='')
print(list(itertools.combinations_with_replacement('GfG',2)))

#count(start,step):
print(list(itertools.count(5,2)))

#cycle():
print(list(itertools.cycle([1,2,3,4])))

#repeat():
print("printing the numbers repeatedly:", end='')
print(list(itertools.repeat(25,4)))

#tee()
l=[2,4,6,7,8,10,20]
iti=iter(l) #store l in iterator
it=itertools.tee(iti,3)
print("The iterators are:")
for i in range (3):
	print(list(it[i]))