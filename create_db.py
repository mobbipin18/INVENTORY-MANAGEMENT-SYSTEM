import sqlite3
def create_db():
    con=sqlite3.connect(database=r"ims.db")
    cur=con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS instock(item_code INTEGER PRIMARY KEY AUTOINCREMENT, item_name, item_type, item_price, availability, cost_price)')
    con.commit()

create_db()


def create_db():
    con=sqlite3.connect(database=r"ims1.db")
    cur=con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS socialform(item_code INTEGER PRIMARY KEY AUTOINCREMENT, item_name, customer_name, customer_contact, followed_by, status)')
    con.commit()

create_db()

def create_db():
    con=sqlite3.connect(database=r"ims2.db")
    cur=con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS releaseform(customer_name,customer_contact,item_code INTEGER PRIMARY KEY AUTOINCREMENT, quantity, address, remarks)')
    con.commit()

create_db()
    
def create_db():
    con=sqlite3.connect(database=r"ims3.db")
    cur=con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS classorder(item_code INTEGER PRIMARY KEY AUTOINCREMENT, item_name, item_type , customer_name, followed_by, customer_contact)')
    con.commit()

create_db()