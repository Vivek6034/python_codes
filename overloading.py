class myclas:
    def __init__(self,para):
       self.para = para 
       
    def __add__(self,other):
        return  self.para + other.para
    
ob1 = myclas(100)
ob2 = myclas(200)
print(ob1+ob2)