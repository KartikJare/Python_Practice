import threading

def Dispaly():
    print("Inside Display function : ",threading.get_ident())
    for i in range(10):
        print("Inside Dispaly")
        
def main():
    print("Inside main : ",threading.get_ident())
    
    t1 = threading.Thread(target=Dispaly)
    t1.start()
    
    t2 = threading.Thread(target=Dispaly)
    t2.start()
    
    t1.join()
    t2.join()
        
    print("End of main")

if __name__ == "__main__":
    main()  