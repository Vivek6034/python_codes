class SBI:
    def SBIroi(self,amt):
        self.amt = amt
        self.ir=self.amt*7.8/100
        print("SBI ROI = ", self.ir)

class ICICI:
    def ICICIroi(self , amt ):
        self.amt  = amt 
        self.ir = self.amt*9.8/100
        print("ICICI ROI = " , self.ir)
class HDFC:
    def HDFCroi(self , amt ):
        self.amt  = amt 
        self.ir = self.amt*12.8/100
        print("HDFC ROI = " , self.ir)

class BANK(SBI,ICICI,HDFC):
    pass
obj = BANK()
amount = int(input("Enter your amount : "))
obj.SBIroi(amount)
