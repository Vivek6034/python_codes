class myclass:
    def __init__(self):
        print("this is constructor ")

    def func1(self):
        print("this is noormal fun")

    def __del__(self):
        print("this is distructor calling ")

ob = myclass()