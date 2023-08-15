x = set()
s = {12,34,65,77,77,77,77,77}
print(s)
print(34 in s)
print(3 in s)
s.remove(77)
print(s)
s1 = {23,54,76,89}
s2 ={51,68,52,75}
print(s1.union(s2))
print(s1.difference(s2))