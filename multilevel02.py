class RBI:
    def rbiroi(self):
        accno = 12345
        bal = 765895
        ir = bal*0.1
        return ir
    
class SBI(RBI):
    def sbiroi(self):
        return "7%"

class PNB(SBI):
    def pnroi(self):
        return "6%"
    
class ICICI(PNB):
    def iciciroi(self):
        return "12%"
    
ob= ICICI()
print("ir of sbi " ,ob.rbiroi())