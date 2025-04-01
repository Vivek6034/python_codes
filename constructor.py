class myclass:
    def __init__(self,fnm , lnm):
        self.fnm=fnm
        self.lnm=lnm
        print("hello world")
    def myfun(self):
        print("user define ", self.fnm, self.lnm)

ob = myclass("vivek " , "singh")
ob.myfun()
    
