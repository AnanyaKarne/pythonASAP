### Arithmetic:
- when dividing two numbers, it doesnt know if it is going to be a float oe int so it takes it as float from the begining
    - you can change the DT to int by *int(x/y)*
### String:
- type(), will give you the datatype of the variable
- ord('x') OR ord(), shows the ordinal value of the character
### conditional
- you cant write expressions on the both side of the conditional operator(e.g. z < x-2 is right  but z-2 < x+2 isnt)
- or, and, not
- when we make any expression and use and, or and not in it, the order to be places in the expression should be 
  - not
  - and
  - or
### Collections
- Lists- in [ ]
  - Mutable-can be changed
  - order collection- the oreder in which we enter things matter and is MAintained as it is
  - list of elements
  - can be of different DT  
  - len(x), will tell the length or the no. of elements  in the list
  - print(x), to print elements 
  - x.append('new), to add elements
  - x.extend([true,34,'fff']), will join this list to the x list
  - x.pop(), will remove the last element
  - x.pop(3), will remove 4th element
  - print(x[2]), will print 3rd element
  - x[2]='new value', will change the value at index 2
  - #to copy the list into the new list, so the changes ina list dont affect the other one, DO:
     z=x[:]
- Tuples
  - immutable
  - cant append, remove, change elements
- You can have list in a list, a tuple in list,etc.
  - [ [],(),[[23,'erw']]]
# Loops
- for loops
  - for i in range(5), will print from 0 t 4, wont include 5
  - range(), is a function, creates a collection of that the input we give
    - range takes parameters as -start, stop, step. and when we give one i/p it by default takes it as stop
  - for i, element in enumerate(x):
    print(i, element), will print the list elements with their index no.
# Set
- unique collection-no duplicate, dont keep track of freq or order of elements
- performing in set rather than others is faster, deleting, searching, etc.
- to create a set do, s = {23,4,5,3}
- and to create an empty set, first make a constructor or you will end up making a dectionary
  - x = set()
  - s = { } 
# Dictionary
- Key value pairs
- this also uses hash, so its fast
- for printing the values of dict-
  - for key , value in d.items():
    print(key, value)
# Unpack operator 
- x = [32,43,31,43323]
  - print(x)
  - print(*x) 
  - this is an unpack operator, it unpacks all the elements of the list individual elements
# F string
- if you want to embbed something without concatenation use f'aekeudfhsrdh' and you can add multiple ____ without using "+"