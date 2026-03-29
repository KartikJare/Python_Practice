class Parent:
    def __init__(self):
        print("Inside parent constructor")
        self.No1 = 10
        self.No2 = 20

    def fun(self):
        print("Inside fun method of parent : ",self.No1,self.No2)

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Inside child Constructor")
        self.A = 11
        self.B = 21

    def sun(slef):
        print("Inside sun method of child : ",slef.A,slef.B,slef.No1,slef.No2) # 11,21,10,20

cobj = Child()

print(cobj.No1) # 10
print(cobj.No2) # 20

print(cobj.A) # 11
print(cobj.B) # 21

cobj.fun()
cobj.sun()