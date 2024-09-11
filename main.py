#file  -- main.py --
import sqliteEz

def main():
    bd = sqliteEz.sqliteEz()
    bd.addFoods("Салат")
    #print(bd.getColumnValueByCondition("Foods", "ID", 5, "Name"))
if __name__ == "__main__":
    main()