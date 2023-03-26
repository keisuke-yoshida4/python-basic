import sqlite3

con = sqlite3.connect("sample.db")
cursor = con.cursor()

target_name = input("Whose 'age' do you want to update?:")
new_age = input("Tell me new age:")
print(target_name, new_age)
# 脆弱性あり
# update_query = f"UPDATE User SET age = {new_age} Where name = '{target_name}'"
# cursor.executescript(update_query)
update_query = 'UPDATE User SET age = ? WHERE name = ?'
cursor.execute(update_query, (new_age, target_name))
con.commit()