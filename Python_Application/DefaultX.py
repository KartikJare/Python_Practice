
def EmployeesInfo(Name,Age,Salary,City = "Mumbai"):
    print("Name : ",Name)
    print("Age : ",Age)
    print("Salary : ",Salary)
    print("City : ",City)

def main():

    EmployeesInfo("Rahul",26,2000.50)
    EmployeesInfo("Rahul",26,2000.50,"Pune")

if __name__ == "__main__":
    main()    
