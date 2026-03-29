No = 11          # Gobal 

def Fun():
    No = 21      # Local
    print("Value of No form Fun is : ",No)  # 21

print("Value of No is : ",No)    # 11
Fun()