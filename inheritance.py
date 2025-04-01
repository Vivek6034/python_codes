class myclassA:
    def func1(self):
        print("this is base classs or parent class ")

class myclassB(myclassA):
    def func2(self):
        print("this is derived or child class ")

obj = myclassB()
obj.func1()
obj.func2()