import sqlite3
con = sqlite3.connect("meta.db", check_same_thread=False)
cur = con.cursor()
sql = "DROP TABLE USER"
result = cur.execute(sql)
con.commit()

sql = "DROP TABLE FILE"
result = cur.execute(sql)
con.commit()

sql = "DROP TABLE LOCK"
result = cur.execute(sql)
con.commit()

sql = "DROP TABLE DATANODE"
result = cur.execute(sql)
con.commit()

