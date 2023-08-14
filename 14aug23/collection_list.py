#Here we're gonna talk about just lists and tuples
#Lists- in [ ]
x = [32, True,'senpai']
print(len(x))
print(x)
x.append('new')
print(x)
x.extend([23,False, 'rafs',234,324])
print(x)
print(x.pop())
print(x)
print('removing-',x.pop(3))
print(x)
print(x[2])
x[2]=False
print(x)
y=x
print(x,y)
#to copy the list into the new list, so the changes ina list dont affect the other one, DO:
z=x[:]
x[3]='lol'
print(x,z)