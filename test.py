import sqlite3
bd=sqlite3.connect(r"./Logins/bd")
cursor=bd.cursor()

cursor.execute("""CREATE TABLE LOGINS (ID text, login text, password text,name text,surname text, motd text)""")
# cursor.execute("""INSERT INTO logins VALUES ()'""")






bd.commit()





