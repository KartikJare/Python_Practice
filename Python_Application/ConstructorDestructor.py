import gc

class Demo:
    def __init__(self):
        print("Inside constructor")

    def __del__(slef):
        print("Inside destructor")    

 # Allocate
obj = Demo()                  # Memory gets allocated

# Use

# Deallocate
del obj

gc.collect()                  # Request to the garbage collector

print("End of application")