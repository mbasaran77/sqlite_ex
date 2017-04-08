import sqlite3

conn = sqlite3.connect('lite.db')
cur = conn.cursor()
# cur.execute("DROP TABLE child")
cur.execute("CREATE TABLE IF NOT EXISTS child(id INTEGER PRIMARY KEY, name TEXT)")
cur.execute("CREATE TABLE IF NOT EXISTS dog(id INTEGER PRIMARY KEY, dog TEXT)")
cur.execute("CREATE TABLE IF NOT EXISTS child_dog(child_id INTEGER, dog_id INTEGER, FOREIGN KEY (child_id) REFERENCES child(id), FOREIGN KEY (dog_id) REFERENCES dog(id) ON UPDATE action)")

# cur.execute("INSERT INTO child VALUES(NULL,'dady')")
boby_id = cur.lastrowid
# cur.execute("INSERT INTO dog VALUES(NULL,'fell')")
dog_id = cur.lastrowid
# cur.execute("INSERT INTO child_dog VALUES(?,?)",(boby_id,dog_id))
# conn.commit()


print(boby_id,dog_id)
def view_data(table_name):
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM {tn}".format(tn=table_name))
    rows = cur.fetchall()
    print(rows)

view_data('child')
view_data('dog')
view_data('child_dog')



# print(boby_id)


conn.commit()
conn.close()
