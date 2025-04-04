class BANK:
    def Rbiroi(self, amt):
        self.amt = amt
        self.ir = self.amt*7.8/100
        print("RBI ROI ", self.ir)
 
class SBIBANK(BANK):
    def sbiroi(self, amt):
        self.amt = amt
        self.ir = self.amt*9/100
        print("SBI ROI ", self.ir)

class ICICIBANK(BANK):
    def ICICiroi(self, amt):
        self.amt = amt
        self.ir = self.amt*12/100
        print("ICICI ROI ", self.ir)

obj = ICICIBANK()
obj.ICICiroi(12000)
obj.Rbiroi(2000)