class Demo:
    def __init__(self):
        print("Inside constructor")

    def __del__(slef):
        print("Inside destructor")    

obj = Demo()

print("End of application")