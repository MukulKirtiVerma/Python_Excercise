# -*- coding: utf-8 -*-
"""
Created on Fri May  8 18:18:28 2020

@author: Mukul Kirti Verma
"""

import itertools

"""
list of itertools functions
 'accumulate',
 'chain',
 'combinations',
 'combinations_with_replacement',
 'compress',
 'count',
 'cycle',
 'dropwhile',
 'filterfalse',
 'groupby',
 'islice',
 'permutations',
 'product',
 'repeat',
 'starmap',
 'takewhile',
 'tee',
 'zip_longest'
 
 """

#accumulate
"""
itertools.accumulate(iterable[, func, *, initial=None])
Make an iterator that returns accumulated sums, or accumulated results of other binary functions (specified via the optional func argument).
"""
print(list(itertools.accumulate([1,2,3,5,6])))


#chain
"""
itertools.chain(*iterables)
Make an iterator that returns elements from the first 
iterable until it is exhausted, then proceeds to the next 
iterable, until all of the iterables are exhausted. 
Used for treating consecutive sequences as a single sequence. 
"""
print(list(itertools.chain([1,2,3,5,6],[8,9])))

#combination
"""
itertools.combinations(iterable, r)
Return r length subsequences of elements from the input iterable.

Combinations are emitted in lexicographic sort order. So, if the input iterable is sorted, the combination tuples will be produced in sorted order.
"""
print(list(itertools.combinations([1,2,3,5,6],3)))


#combinations_with_replacement
"""
itertools.combinations_with_replacement(iterable, r)
Return r length subsequences of elements from the input iterable allowing individual elements to be repeated more than once.
"""
print(list(itertools.combinations_with_replacement([1,2,3,5,6],3)))


#compress
"""
itertools.compress(data, selectors)
Make an iterator that filters elements from data returning only 
those that have a corresponding element in selectors 
that evaluates to True. Stops when either the data or 
selectors iterables has been exhausted. Roughly equivalent to:
"""
print(list(itertools.compress([1,2,3,5,6],[1,0,0,0,1])))

#cycle
"""
itertools.cycle(iterable)
Make an iterator returning elements from the iterable and 
saving a copy of each. When the iterable is exhausted, 
return elements from the saved copy.
"""
j=0
for i in itertools.cycle([1,2,3,5,6]):
    print(i)
    if(j==100):
        break
    j+=1
    


#dropwhile
"""
itertools.dropwhile(predicate, iterable)
Make an iterator that drops elements from the iterable as 
long as the predicate is true; afterwards, returns 
every element. Note, the iterator does not produce any 
output until the predicate first becomes false, so it 
may have a lengthy start-up time. 
"""
def fun(x):
    if(x<5):
        return True
    return False
for i in itertools.dropwhile(fun,[1,2,3,5,6]):
    print(i)
   
#filterfalse
"""
itertools.filterfalse(predicate, iterable)
Make an iterator that filters elements from iterable 
returning only those for which the predicate is False. 
If predicate is None, return the items that are false.
"""
def fun(x):
    if(x<5):
        return True
    return False
for i in itertools.filterfalse(fun,[1,2,3,5,6]):
    print(i)
    
    
#groupby
"""
itertools.groupby(iterable, key=None)
Make an iterator that returns consecutive keys 
and groups from the iterable. The key is a function
 computing a key value for each element. If not specified
 or is None, key defaults to an identity function and returns
 the element unchanged. Generally, the iterable needs to
 already be sorted on the same key function.
"""

def fun(x):
    import random
    return random.randint(1,10)
print(list(itertools.groupby([1,2,3,5,6,8],fun)))


#islice
"""
itertools.islice(iterable, stop)
itertools.islice(iterable, start, stop[, step])
Make an iterator that returns selected elements from 
the iterable. If start is non-zero, then elements from 
the iterable are skipped until start is reached.
 Afterward, elements are returned consecutively unless 
 step is set higher than one which results in items being 
 skipped. If stop is None, then iteration continues until 
 the iterator is exhausted, if at all; otherwise, it stops 
 at the specified position. Unlike regular slicing, islice() 
 does not support negative values for start, stop, or step.
 """
 
print(list(itertools.islice([1,2,3,5,6],5)))


#permutations
"""
itertools.permutations(iterable, r=None)
Return successive r length permutations of elements in the 
iterable.
"""
print(list(itertools.permutations([1,2,3,5,6],3)))

#product
"""
itertools.product(*iterables, repeat=1)
Cartesian product of input iterables.
Roughly equivalent to nested for-loops in a generator 
expression. For example, product(A, B) returns the same 
as ((x,y) for x in A for y in B).

"""

print(list(itertools.product([1,2,3],[4,5,6])))

#repeat
"""
itertools.repeat(object[, times])
Make an iterator that returns object over and over again. 
Runs indefinitely unless the times argument is specified. Used as argument to map() for invariant parameters to the called function. Also used with zip() to create an invariant part of a tuple record.
"""

print(list(itertools.repeat([1,2,3],3)))

#starmap
"""
itertools.starmap(function, iterable)
Make an iterator that computes the function using arguments 
obtained from the iterable. Used instead of map() when 
argument parameters are already grouped in tuples from a 
single iterable (the data has been “pre-zipped”). 
The difference between map() and starmap() parallels 
the distinction between function(a,b) and function(*c).
"""

for i in itertools.starmap(pow,[(1,2),(3,4)]):
    print(i)
     
#takewhile
"""
itertools.takewhile(predicate, iterable)
Make an iterator that returns elements from the iterable as long as the predicate is true. Roughly equivalent to:
"""
for i in itertools.takewhile(lambda x: x<5, [1,4,6,4,1]):
    print(i)
    
    
#tee
"""
itertools.tee(iterable, n=2)
Return n independent iterators from a single iterable.
The following Python code helps explain what tee does 
(although the actual implementation is more complex and 
uses only a single underlying FIFO queue).
"""

for i in itertools.tee([1,2,3,4,5],2):
    for j in i:
        print(j)
        
 
#zip_longest       
"""
itertools.zip_longest(*iterables, fillvalue=None)
Make an iterator that aggregates elements from each of
 the iterables. If the iterables are of uneven length,
 missing values are filled-in with fillvalue. Iteration 
 continues until the longest iterable is exhausted. 
"""


for i in itertools.zip_longest([1,3,3,4,5],[1,9,5,8,9],'-'):
    for j in i:
        print(j)
        


