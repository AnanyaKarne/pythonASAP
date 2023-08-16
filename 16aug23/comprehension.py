a = [ a for a in range(5)]
print(a)

b = [b+5 for b in range(5)]
print(b)

c = [c%5 for c in range(20)]
print(c)
 
d = [0 for d in range(5)]
print(d)

e = [[e/2 for e in range(5)]for e in range(2)]
print(e)
#giving 2 lists of the quotients

f = [i for i in range(10) if i%2==0]
print(f)
f = tuple(i for i in range(10) if i%2==0)
print(f)