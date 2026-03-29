import threading

def Dispaly():
    print("Inside Display function : ",threading.get_ident())
    
def main():
    print("Inside main : ",threading.get_ident())
    
    t = threading.Thread(target=Dispaly)
    t.start()
    
    print("End of main")

if __name__ == "__main__":
    main()  