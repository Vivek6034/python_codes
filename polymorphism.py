class classA:
    def myfunction(self):
        print("this is classs A ")

class classB:
    def myfunction(self):
        print("this is classs B ")

class classC:
    def myfunction(self):
        print("this is classs C ")
        
def f(obj):
    obj.myfunction()

obj1 = classC()

f(obj1)
l=[classA(),classB(),classC()]

for i in l:
    f(i)
