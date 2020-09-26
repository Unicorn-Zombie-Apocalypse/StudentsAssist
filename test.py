import sqlite3
bd=sqlite3.connect(r"./Logins/bd")
cursor=bd.cursor()

cursor.execute(("""CREATE TABLE logins (login text, password text)"""))

#cursor.execute("""INSERT INTO * VALUES""")
bd.commit()





