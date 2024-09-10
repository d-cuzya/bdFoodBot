#file  -- sqliteEz.py --
import sqlite3

class sqliteEz:
    #Конструктор
    def __init__(self):
        print("Конструктор")
        self.con = sqlite3.connect("dbBot.db")
        self.cur = self.con.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS foods ("
                         "id INTEGER PRIMARY KEY AUTOINCREMENT, "
                         "name TEXT NOT NULL, "
                         "price INSEGER NOT NULL, "
                         "description TEXT, img TEXT)"
                        ";")
        
    #Деструктор
    def __del__(self):
        print("Деструктор")
        self.con.close()

