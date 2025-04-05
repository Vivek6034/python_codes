class classA:
    def __init__(self):
        print("this is classs A ")

class classB(classA):
    def __init__(self):
        super().__init__()
        print("this is classs B ")

ob = classB()