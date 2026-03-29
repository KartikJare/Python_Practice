
def EmployeesInfo(Name,Age,Salary,City):
    print("Name : ",Name)
    print("Age : ",Age)
    print("Salary : ",Salary)
    print("City : ",City)

def main():
    # Positional
    # EmployeesInfo("Rahul",25,2000.50,"Pune") # Correct
    # EmployeesInfo(26,"Rahul","Pune",2000.50) # Wrong

    # Keyword argument
    EmployeesInfo(Age = 26,Name = "Rahul",City = "Pune",Salary = 2000.50) # Correct
        
if __name__ == "__main__":
    main()    
