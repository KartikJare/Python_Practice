import threading

def Dispaly():
    print("Inside Display function : ",threading.get_ident())
    for i in range(100):
        print("Inside Dispaly")
    
def main():
    print("Inside main : ",threading.get_ident())
    
    t = threading.Thread(target=Dispaly)
    t.start()
    t.join()
        
    print("End of main")

if __name__ == "__main__":
    main()  