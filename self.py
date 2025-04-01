class myclass:
    def display(self,fnm , lnm):
        self.fnm=fnm
        self.lnm=lnm
    def show(self):
        print("hello display function is calling =",self.fnm,self.lnm)


obj = myclass()
n1 = int(input("enter s 1st num : "))
n2 = int(input("enter a 2nd num "))
obj.display(n1,n2)
obj.show()
            
 #wap to make a calculator self and return type with 
 # argument fumction input taken from user 


