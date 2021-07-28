CREATE TABLE IF NOT EXISTS Costumers  (
    Id INTEGER PRIMARY KEY,
    Name TEXT,
    Age INTEGER,
    Address TEXT
);

CREATE TABLE IF NOT EXISTS Employees (
    Id INTEGER PRIMARY KEY,
    Name TEXT,
    Age INTEGER,
    Address TEXT,
    Wage REAL
);

CREATE TABLE IF NOT EXISTS Products (
    Id INTEGER PRIMARY KEY,
    Name TEXT,
    Price REAL,
    stock_quantity INTEGER
);

CREATE TABLE IF NOT EXISTS Sales (
    Id_sales INTEGER PRIMARY KEY,
    Id_product INTEGER,
    Id_costumer INTEGER,
    Quantity INTEGER,
    Final_Price REAL,
    datetimeStamp TEXT,
    FOREIGN KEY (Id_product) REFERENCES Products(Id),
    FOREIGN KEY (Id_costumer) REFERENCES Costumers (Id)
);