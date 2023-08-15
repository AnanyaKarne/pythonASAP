d = {'a' : 432, 'b': 565}
print(d['b'])
d[2] = 'dfs'
d['re'] = [543,65,65,4]
# print(d)
# print('a' in  d)
# print(d.values())
# print(list(d.values()))
for key, value in d.items():
    print(key, value)

for key in d:
    print(key, d[key])