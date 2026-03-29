import gc

class Demo:
    def __init__(self):
        print("Inside constructor")

    def __del__(slef):
        print("Inside destructor")    

 # Allocate
obj1 = Demo()                  # Memory gets allocated
obj2 = Demo()

# Use

# Deallocate
del obj1
del obj2


gc.collect()                  # Request to the garbage collector

print("End of application")