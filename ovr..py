class mycls:
    def __init__(self,para):
        self.para = para

    def __mul__(self,other):
        return self.para*other.para
    
ob1 = mycls(100)
ob2 = mycls(200)
print(ob1*ob2)

class mycls:
    def __init__(self,para):
        self.para = para

    def __add__(self,other):
        return self.para+other.para
    
ob1 = mycls(200)
ob2 = mycls(300)
print(ob1+ob2)

class mycls:
    def __init__(self,para):
        self.para = para

    def __le__(self,other):
        return self.para<=other.para
    
ob1 = mycls(100)
ob2 = mycls(200)
print(ob1<=ob2)


class mycls:
    def __init__(self,para):
        self.para = para

    def __lt__(self,other):
        return self.para<other.para
    
ob1 = mycls(100)
ob2 = mycls(200)
print(ob1<ob2)