import sqlite3
from sqlite3 import Error
from sqlite3.dbapi2 import Cursor
from time import strftime
from uuid import uuid1

class TaskDatabase:

    def __init__(self, name):
        '''Instantiates SQLite3 Database as a python object'''
        self.name = name
        self.path = f'{self.name}.db'
        self.table = self.getTables()

        connector = None
        try:
            connector = sqlite3.connect(self.path)
        except Error as error:
            assert f'{error}'
        finally:
            if connector:
                self.executeScript('schema.sql')
                connector.close()

    def getTables(self):
        '''
        Returns:
            list: a list with the tables inside the database
        '''
        try:
            connector = sqlite3.connect(self.path)
            cursor = connector.cursor()
            cursor.execute('SELECT name FROM sqlite_master WHERE type="table";')
            query = cursor.fetchall()

            retData = [data[0] for data in query]
            return retData
        
        except Error as error:
            assert f'{error}'

        finally:
            if connector:
                connector.close()

    def executeScript(self, scriptPath):
        '''Executes a .sql script in the database instance

        Args:
            script_path (str): path to the .sql script
        '''
        try:
            connector = sqlite3.connect(self.path)
            cursor = connector.cursor()
            cursor.executescript(open(scriptPath).read())

        except Error as error:
            assert f'{error}'

        finally:
            if connector:
                connector.close()
        
    def registerProduct(self, name, price, stock_quantity):
        """[Registers a product in database]

        Args:
            name ([string]): [name of the product]
            price ([float]): [price of the product]
            stock_quantity ([int]): [quantity of product in stock]
        """        
        connector = None
        try:
            connector = sqlite3.connect(self.path)
            cursor = connector.cursor()
            cursor.execute(
                f'INSERT INTO Products (Id, Name, Price, stock_quantity) VALUES (?,?,?,?);',
                (uuid1().int>>100,name,price, stock_quantity)
                )
            connector.commit()
        
        except Error as error:
            print(error)

        finally:
            if connector:
                connector.close()

    def registerEmployee(self, name, age, address, wage):

        connector = None
        try:
            connector = sqlite3.connect(self.path)
            cursor = connector.cursor()

            cursor.execute(
                f'INSERT INTO Employees (id, name, age, address, wage) VALUES (?,?,?,?,?);',
                (uuid1().int>>100,name,age,address,wage)
                )
            connector.commit()
        
        except Error as error:
            print(error)

        finally:
            if connector:
                connector.close()

    def registerCostumer(self, name, age, address):

        connector = None
        try:
            connector = sqlite3.connect(self.path)
            cursor = connector.cursor()
            
            cursor.execute(
                f'INSERT INTO Costumers (id, name, age, address) VALUES (?,?,?,?);',
                (uuid1().int>>100,name,age,address)
            )
            connector.commit()
        
        except Error as error:
            print(error)
    
        finally:
            if connector:
                connector.close()

    def listProducts(self):

        connector = None
        try:
            connector = sqlite3.connect(self.path)
            cursor = connector.cursor()

            cursor.execute('SELECT * FROM Products ORDER BY Id;')

            query = cursor.fetchall()

            for row in query:
                print(row)
        
        except Error as error:
            print(error)

        finally:
            if connector:
                connector.close()
    
    def listCostumers(self):

        connector = None
        try:
            connector = sqlite3.connect(self.path)
            cursor = connector.cursor()

            cursor.execute('SELECT * FROM Costumers ORDER BY Id;')

            query = cursor.fetchall()

            for row in query:
                print(row)
        
        except Error as error:
            print(error)

        finally:
            if connector:
                connector.close()
    
    def listEmployees(self):

        connector = None
        try:
            connector = sqlite3.connect(self.path)
            cursor = connector.cursor()

            cursor.execute('SELECT * FROM Employees ORDER BY Id;')

            query = cursor.fetchall()

            for row in query:
                print(row)
        
        except Error as error:
            print(error)


        finally:
            if connector:
                connector.close()
    
    def listSales(self):

        connector = None
        try:
            connector = sqlite3.connect(self.path)
            cursor = connector.cursor()
            cursor.execute('SELECT * FROM Sales ORDER BY datetimeStamp;')

            query = cursor.fetchall()
            for row in query:
                print(row)
        
        except Error as error:
            print(error)

        finally:
            if connector:
                connector.close()
    
    def registerSale(self, Id_product, Id_costumer, Quantity):

        connector = None
        try:
            connector = sqlite3.connect(self.path)
            cursor = connector.cursor()

            command = f'SELECT stock_quantity FROM Products WHERE Id = {Id_product};'
            cursor.execute(command)
            befSaleQuantity = cursor.fetchall()[0][0]
            
            command = f'SELECT Name From Costumers WHERE Id = {Id_costumer};'
            cursor.execute(command)
            CostumerName = cursor.fetchall()[0][0]

            command = f'SELECT Id FROM Employees WHERE Name = "{CostumerName}";'
            cursor.execute(command)
            isEmployee = True if cursor.fetchall() else False

            command = f'SELECT price FROM Products WHERE Id = {Id_product};'
            cursor.execute(command)
            price = cursor.fetchall()[0][0]
            
            if befSaleQuantity >= Quantity:
                Final_Price = Quantity*price*0.9 if isEmployee else Quantity*price
                cursor.execute(
                    f'INSERT INTO Sales (Id_sales, Id_product, Id_costumer, Quantity, Final_Price, datetimeStamp) VALUES ({uuid1().int>>64},{Id_product},{Id_costumer},{Quantity},{Final_Price},"{strftime("%d/%m/%Y - %H:%M:%S")}");')
                connector.commit()
                command = f'UPDATE Products SET stock_quantity={befSaleQuantity - Quantity} WHERE Id={Id_product};'
                cursor.execute(command)
                connector.commit()
            else:
                print(f"You're trying to sell more products then we have in stock")

        except Error as error:
            print(error)

        finally:
            if connector:
                connector.close()