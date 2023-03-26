import sqlite3

con = sqlite3.connect("sample.db")
cursor = con.cursor()

for row in cursor.execute("SELECT * FROM User"):
    print(row)

print("---" * 30)
cursor.execute("SELECT * FROM User")
# print(cursor.fetchall())
print("---" * 30)
print(cursor.fetchone())
