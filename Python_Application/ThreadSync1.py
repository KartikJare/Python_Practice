import threading

iCnt = 0

def Update():
    global iCnt

    for _ in range(2000000):   # _ is for empty space i do not need local variable
        iCnt = iCnt + 1

def main():
    global iCnt 
    
    Update() #200000
    Update() #400000

    print("Value of icnt  is :",iCnt)

if __name__ == "__main__":
    main()