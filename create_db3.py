import sqlite3
def create_db():
    con=sqlite3.connect(database=r"ims3.db")
    cur=con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS classorder(item_code INTEGER PRIMARY KEY AUTOINCREMENT, item_name, item_type , customer_name, followed_by, customer_contact)')
    con.commit()

create_db()

