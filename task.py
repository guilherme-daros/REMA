from os import name
from dbclass import TaskDatabase

db = TaskDatabase('teste')
MENU = """
Type 1 to create a new product
Type 2 to show registered products
Type 3 to create a new employee
Type 4 to show registered employees
Type 5 to create a new customer
Type 6 to show registered customers
Type 7 to create a new sale
Type 8 to show registered sales
        """

while True:
    sel = 0
    if sel not in (1,2,3,4,5,6,7,8):
        print(MENU)
        try:
            sel = int(input("Option: "))
            if sel not in (1,2,3,4,5,6,7,8):
                print("Option must be between 1 and 8")
                
        except:
            print("Option must be a number from 1 to 8")

    if sel == 1:
        name = str(input("name: "))
        price = float(input("price: "))
        stock = int(input("stock quantity: "))
        db.registerProduct(name, price, stock)

    elif sel == 2:
        db.listProducts()

    elif sel == 3:
        name = str(input("name: "))
        age = int(input("age: "))
        address = str(input("adress: "))
        wage = float(input("wage: "))
        db.registerEmployee(name,age,address,wage)
    
    elif sel == 4:
        db.listEmployees()

    elif sel == 5:
        name = str(input("name: "))
        age = int(input("age: "))
        address = str(input("adress: "))
        db.registerCostumer(name,age,address)

    elif sel == 6:
        db.listCostumers()

    elif sel == 7:
        Id_product = int(input("Product ID: "))
        Id_costumer = int(input("Costumer ID: "))
        Quantity = int(input("Quantity: "))
        db.registerSale(Id_product,Id_costumer,Quantity)

    elif sel == 8:
        db.listSales()
