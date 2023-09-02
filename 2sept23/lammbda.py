x = lambda x, y: x+y
print(x(2,2))

a = [21,3,4,5,78,2,34,6,3,63,65,78,7,32,2,5,648,53,47,14,47]
mp = map(lambda i: i+1, a)
print(list(mp))
mp = filter(lambda i: i%2==0, a)
print(list(mp))