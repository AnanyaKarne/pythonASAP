# x = [32,43,31,43323]
# print(x)
# print(*x) ## this is an unpack operator, it unpacks all the elements of the list individual elements

# def testt(x, y):
#     print(x,y)

# h=[(11,22),(33,44)]

# print(h)
# print("using unpack operator")
# for hi in h:
#     testt(*hi)

# print("In case of dictionary we need two astric('*')")
# testt(**{'x':32, 'y':787})

print("NOW THE ARGS AND KWARGS")

def argkw(*args, **kwargs):
    print(args, kwargs)
    print(args)
    print(kwargs)
argkw(32,4,365,67,75, a=3, b=32)
# print()

# def dun(a, b):
#     print(a,b)
# one = [(2,3), (32,334)]
# for onii in one:
#     dun(*onii)


