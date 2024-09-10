#file  -- sqliteEz.py --
import sqlite3

class sqliteEz:
    #Конструктор
    def __init__(self):
        #print("Конструктор")
        self.con = sqlite3.connect("dbBot.db")
        self.cur = self.con.cursor()
        #Вкючние ссылок на другие таблицы
        self.cur.execute("PRAGMA foreign_keys = ON;")
        #Создание таблицы "Foods"
        self.cur.execute("CREATE TABLE IF NOT EXISTS Foods ("
                         "ID INTEGER PRIMARY KEY AUTOINCREMENT, "
                         "Name TEXT NOT NULL, "
                         "Description TEXT, "
                         "Price INTEGER, "
                         "Img TEXT"
                         ");")
        #Создание таблицы "UserList"
        self.cur.execute("CREATE TABLE IF NOT EXISTS UserList ("
                         "ID INTEGER PRIMARY KEY AUTOINCREMENT, "
                         "FirstName TEXT NOT NULL, "
                         "SecondName TEXT NOT NULL "
                         ");")
        #Создание таблицы "CurrentOrders"
        self.cur.execute("CREATE TABLE IF NOT EXISTS CurrentOrders ("
                         "ID INTEGER PRIMARY KEY AUTOINCREMENT, "
                         "OrderID INTEGER NOT NULL, "
                         "UserID INTEGER NOT NULL, "
                         "PaidFor INTEGER NOT NULL DEFAULT 0, " #Оплаченный ли заказ, 1 - true, 0 - false, Default: 0
                         "Completed INTEGER NOT NULL DEFAULT 0" #Выполнен ли заказ, 1 - true, 0 - false, Default: 0
                         "FOREIGN KEY (OrderID) REFERENCES Foods(ID), "
                         "FOREIGN KEY (UserID) REFERENCES UserList(ID), "
                         ");")
        #Создание таблицы "History"
        self.cur.execute("CREATE TABLE IF NOT EXISTS History ("
                         "ID INTEGER PRIMARY KEY AUTOINCREMENT, "
                         "OrderID INTEGER NOT NULL, "
                         "CurrentUserID INTEGER NOT NULL, "
                         "FOREIGN KEY (OrderID) REFERENCES Foods(ID), "
                         "FOREIGN KEY (CurrentUserID) REFERENCES CurrentOrders(ID) "
                         ");")
        
    #Деструктор
    def __del__(self):
        #print("Деструктор")
        self.con.close()

