import psycopg2
# conn = psycopg2.connect('lite.db')
# cur = conn.cursor()
# cur.execute('pragma foreign_keys=ON')



def create_table():
    conn = psycopg2.connect("dbname = 'database1' user = 'postgres' password = '1' host = 'localhost' port = '5432' ")
    cur = conn.cursor()
    # cur.execute('pragma foreign_keys=ON')

    # cur.execute("CREATE TABLE IF NOT EXISTS kitap(kitap_id INTEGER PRIMARY KEY NOT NULL, kitap_name TEXT, kitap_yazar INTEGER NOT NULL,"
    # "adet INTEGER, fiyat REAL,FOREIGN KEY (kitap_yazar) REFERENCES yazar_tablo(yazar_id))")
    cur.execute("CREATE TABLE IF NOT EXISTS kitap(kitap_id INTEGER PRIMARY KEY NOT NULL, kitap_name TEXT, kitap_yazar INTEGER NOT NULL,"
    "adet INTEGER, fiyat REAL)")
    conn.commit()
    conn.close()

def view_data(table_name):
    conn = psycopg2.connect('lite.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM {tn}".format(tn=table_name))
    # cur.execute("SELECT * FROM yazar_ad")
    rows = cur.fetchall()
    conn.close()
    return rows

def insert_data(kitap_id,kitap_adi,yazar_id,adet,fiyat):
    conn = psycopg2.connect('lite.db')
    cur = conn.cursor()
    cur.execute('pragma foreign_keys=ON')

    # cur.execute("INSERT INTO kitap VALUES(?,?,?,?,?)",(kitap_id,kitap_adi, yazar_id, adet,fiyat))
    cur.execute("INSERT INTO kitap(kitap_name,kitap_yazar,adet,fiyat) VALUES(?,?,?,?)",(kitap_adi, yazar_id, adet,fiyat))
    conn.commit()
    conn.close()

def delete_data(data):
    conn = psycopg2.connect('lite.db')
    cur = conn.cursor()
    cur.execute("DELETE  FROM kitap WHERE kitap_name=? ",(data,))
    conn.commit()
    conn.close()

def update_data(kitap_adi,adet,fiyat):
    conn = psycopg2.connect('lite.db')
    cur = conn.cursor()
    cur.execute("UPDATE kitap SET adet = ?, fiyat = ?  WHERE kitap_name= ?",(adet,fiyat,kitap_adi))
    conn.commit()
    conn.close()
def create_table_yazar():
    conn = psycopg2.connect('lite.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS yazar_tablo(yazar_id INTEGER PRIMARY KEY NOT NULL, yazar_ad TEXT)")
    conn.commit()
    conn.close()

def delete_table(table_name):
    conn = psycopg2.connect('lite.db')
    cur = conn.cursor()
    cur.execute("DROP TABLE {tn}".format(tn=table_name))
    conn.commit()
    conn.close()
def rec_yazar(yazar_id, yazar_ad):
    conn = psycopg2.connect('lite.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO yazar_tablo VALUES(?,?) ",(yazar_id,yazar_ad))
    conn.commit()
    conn.close()

def yazar_kitap_sorgu(yazar_adi):
    conn = psycopg2.connect('lite.db')
    cur = conn.cursor()
    cur.execute("SELECT yazar_id FROM yazar_tablo WHERE yazar_ad =(?) ",(yazar_adi,))
    yazar_id = cur.fetchone()
    print("yazar_id: ",yazar_id[0])
    cur.execute("SELECT kitap_name FROM kitap WHERE kitap_yazar=(?)",(yazar_id))
    yazar_ad = cur.fetchall()
    text =""
    i = 0
    for a in yazar_ad:
        text += str(i) + "-" + a[0] + " "
        i += 1
    print(text)


# delete_table("kitap")
create_table()
# create_table_yazar()
# insert_data(2,"bir ada hikayesi 2",1,15,15.0)
# insert_data(2,"bozkurtlar",2,15,15.0)
# insert_data(2,"ince mehmed",1,15,15.0)

# delete_data("vadideki zambak")
# rec_yazar(2,"yasar kemal")
# rec_yazar(3,"nihal atsiz")
# print(view_data("kitap"))
# print(view_data("yazar_tablo"))
# yazar_kitap_sorgu('yasar kemal')
# yazar_kitap_sorgu('nihal atsiz')
