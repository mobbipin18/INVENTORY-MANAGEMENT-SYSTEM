import sqlite3
def create_db():
    con=sqlite3.connect(database=r"ims.db")
    cur=con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS instock(item_code INTEGER PRIMARY KEY AUTOINCREMENT, item_name, item_type, item_price, availability, cost_price)')
    con.commit()

create_db()

