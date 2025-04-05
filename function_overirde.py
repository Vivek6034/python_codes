class classA:
    def myfunction(self):
        print("this is classs A ")

class classB(classA):
    def myfunction(self):
        super().myfunction()    # super methood use to prevent from overide
        print("this is classs B ")

class classC(classB):
    def myfunction(self):
        super().myfunction()
        print("this is classs C ")

ob = classC()
ob.myfunction()