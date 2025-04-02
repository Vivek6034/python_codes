class dadaji:
    def dadaji1(self):
        print("property of dada ji")

class pitaji(dadaji):
    def pitaji1(self):
        print("property of pita ji")

class beta(pitaji):
    def betaji1(self):
        print("my property")

ob = beta()
ob.dadaji1()
ob.pitaji1()
ob.betaji1()