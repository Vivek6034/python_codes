class myclass:
    def __init__(self):
        print("this is constructor ")

    def __init__(self,a):
        print("this is one argument constructor ")

    def __init__(self ,a,b,c):
        print("this is third argument constrructor")

ob = myclass(10,20,30)