No = 11          # Gobal 

def Fun():
    global No      # global Keyword we can update the No 
    print("Value of No form Fun is : ",No)  # 11
    No = No + 1  # 12
    print("Value of No form Fun is : ",No)  # 12

print("Value of No is : ",No)    # 11
Fun()
print("Value of No is : ",No)    # 12