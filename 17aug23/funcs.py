def sum(a, b, c):
    print(a+b+c)

sum(3,4,1)

def summ(a, b, c=None):
    return a,b,c
print(summ(23,45))

def lalala(x, y):
    return  x*y, int(x/y)

r1, r2 = lalala(4,2)
print(r1, r2)

