def func(x):
    def func1():
        print(x)
    return func1
print(func(3)) #displays it is a function object
# print(func(23)())
func(23)() #prints value of x->23
s= func(43)
s()
func(3)()
