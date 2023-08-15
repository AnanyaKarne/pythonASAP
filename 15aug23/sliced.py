x = [1,2,3,4,5,6,7,8,9,10]
print(x)
#sliced_list = x[start:stop:step]-- give indexes btwn colons
nimnim = x[1:9:2]
print(nimnim)
nim1 = x[:4]
print(nim1)
nim2 = x[4:]
print(nim2)
nim3 = x[4:1:-1]
print(nim3)
nim4 = x[::-1]
print(nim4)
#also on strings
str = "kawaii"
str1 = str[::-1]
print(str1)
str2 = str[::2]
print(str2)