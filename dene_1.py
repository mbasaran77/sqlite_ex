

import sqlite3
sqlite3.foreign_keys = 1
sqlite3.constraint = 1
def create_table():
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS kitap(kitap_id INTEGER PRIMARY KEY NOT NULL, kitap_name TEXT, kitap_yazar INTEGER NOT NULL,"
    "adet INTEGER, fiyat REAL,FOREIGN KEY CONSTRAINT (kitap_yazar) REFERENCES yazar_tablo(yazar_id))")
    conn.commit()
    conn.close()

def view_data(table_name):
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM {tn}".format(tn=table_name))
    # cur.execute("SELECT * FROM yazar_ad")
    rows = cur.fetchall()
    conn.close()
    return rows

def insert_data(kitap_id,kitap_adi,yazar_id,adet,fiyat):
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    # cur.execute("INSERT INTO kitap VALUES(?,?,?,?,?)",(kitap_id,kitap_adi, yazar_id, adet,fiyat))
    cur.execute("INSERT INTO kitap(kitap_name,kitap_yazar,adet,fiyat) VALUES(?,?,?,?)",(kitap_adi, yazar_id, adet,fiyat))
    conn.commit()
    conn.close()

def delete_data(data):
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("DELETE  FROM kitap WHERE kitap_name=? ",(data,))
    conn.commit()
    conn.close()

def update_data(kitap_adi,adet,fiyat):
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("UPDATE kitap SET adet = ?, fiyat = ?  WHERE kitap_name= ?",(adet,fiyat,kitap_adi))
    conn.commit()
    conn.close()
def create_table_yazar():
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS yazar_tablo(yazar_id INTEGER PRIMARY KEY NOT NULL, yazar_ad TEXT)")
    conn.commit()
    conn.close()

def delete_table(table_name):
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("DROP TABLE {tn}".format(tn=table_name))
    conn.commit()
    conn.close()
def rec_yazar(yazar_id, yazar_ad):
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO yazar_tablo VALUES(?,?) ",(yazar_id,yazar_ad))
    conn.commit()
    conn.close()

delete_table("kitap")
create_table()
# create_table_yazar()
insert_data(2,"denemeler",8,15,15.0)
# delete_data("vadideki zambak")
#update_data('ÖZGÜR YAZILIM',25,50.0)
# rec_yazar(2,"yasar kemal")
# rec_yazar(3,"nihal atsiz")
print(view_data("kitap"))
print(view_data("yazar_tablo"))
print(sqlite3.foreign_keys)
