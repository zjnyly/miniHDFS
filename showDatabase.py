import sqlite3
cursor = sqlite3.connect("meta.db", check_same_thread=False)
cursor = cursor.cursor()


print("FILE")
sql = '''SELECT * FROM FILE;'''

result = cursor.execute(sql,)

lines = result.fetchall()

for line in lines:
    print(line)



print("\nLOCK")
sql = '''SELECT * FROM LOCK;'''

result = cursor.execute(sql,)

lines = result.fetchall()

for line in lines:
    print(line)