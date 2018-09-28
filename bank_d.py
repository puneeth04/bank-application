import sqlite3
from realmadrid import *
conn = sqlite3.connect("bank.db")
c = conn.cursor()


c.execute("""CREATE TABLE IF NOT EXISTS BANKDET(
             ID     INT,
             USERNAME TEXT,
             AMOUNT REAL
             )""")
c.execute("""CREATE TABLE IF NOT EXISTS BANKACC(
             ID      INT,
             USERNAME TEXT,
             PASSWORD TEXT
             )""")





conn.commit()
conn.close()

