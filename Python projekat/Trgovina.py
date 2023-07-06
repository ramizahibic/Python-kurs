import sqlite3

from pip._internal.utils.misc import tabulate

connection=sqlite3.connect("trgovina.db")
cursor=connection.cursor()
sql_comm="""
CREATE TABLE Sjediste(
ID_SJEDISTA INTEGER PRIMARY KEY,
NAZIV_SJEDISTA VARCHAR(50),
LOKACIJA_SJEDISTA VARCHAR(50),
KONTAKT INTEGER
);
"""
cursor.execute(sql_comm)
connection.close()
import sqlite3
connection=sqlite3.connect("trgovina.db")

def unos(ID_SJEDISTA, NAZIV_SJEDISTA,LOKACIJA_SJEDISTA,KONTAKT):
    qry="INSERT INTO Sjediste(ID_SJEDISTA, NAZIV_SJEDISTA, LOKACIJA_SJEDISTA, KONTAKT)VALUES(?,?,?,?);"
    connection.execute(qry,ID_SJEDISTA, NAZIV_SJEDISTA,LOKACIJA_SJEDISTA,KONTAKT)
    connection.commit()
    print("Dodali ste novo sjediste")

def izmjena(ID_SJEDISTA, NAZIV_SJEDISTA, LOKACIJA_SJEDISTA, KONTAKT):
    qry="UPDATE Sjediste set NAZIV_SJEDISTA=?, LOKACIJA_SJEDISTA=?, KONTAKT=?,=? WHERE ID_SJEDISTA=?;"
    connection.execute(qry(NAZIV_SJEDISTA, LOKACIJA_SJEDISTA, KONTAKT,ID_SJEDISTA))
    connection.commit()
    print("Izmijenili ste podatke o sjedistu")
    res=connection.cursor()
    qry="UPDATE Sjediste set NAZIV_SJEDISTA=?, LOKACIJA_SJEDISTA=?, KONTAKT=? WHERE ID_SJEDISTA=?;"
    sjediste=(NAZIV_SJEDISTA,LOKACIJA_SJEDISTA,KONTAKT,ID_SJEDISTA)
    res.execute=(qry,sjediste)
    connection.commit()
    print("Izmijenili ste podatke o sjedist uspjesno")

def brisanje_informacija(ID_SJEDISTA):
    qry="DELETE FROM Sjediste WHERE ID_SJEDISTA=?;"
    connection.execute(qry,(ID_SJEDISTA))
    connection.commit()
    print("Uspjesno ste obrisali podatke o sjedistu")
    res=connection.cursor()
    qry="DELETE FROM Sjediste WHERE ID_SJEDISTA=?;"
    izbrisi=(ID_SJEDISTA)
    res.execute(qry,izbrisi)
    connection.commit()
    print("Podaci su uspjesno obrisani")

def selektovanje_informacija():
    res=connection.cursor()
    qry="SELECT * FROM Sjediste"
    res.execute(qry)
    rezultat=res.fetchall()
    print(tabulate(rezultat,headers=["ID_SJEDISTA", "NAZIV_SJEDISTA","LOKACIJA_SJEDISTA","KONTAKT"]))
    if res.rowcount<0:
        print("Nisu pronadjeni podaci")
    else:
        for podaci in rezultat:
            print(podaci)
print("""
1. Unosenje novih podataka.
2. Promjena podataka.
3. Brisanje podataka.
4. Selektovanje podataka.
""")

unos_podataka=1
while unos_podataka==1:
    unos=int(input("Izaberite opciju:"))
    if(unos==1):
        print("Dodajte novo sjediste")
        ID_SJEDISTA=int(input("Unesite ID:"))
        NAZIV_SJEDISTA=input("Unesite naziv sjedista:")
        LOKACIJA_SJEDISTA=input("Unesite lokaciju sjedista:")
        KONTAKT=int(input("Unesite kontakt: "))
        unos(ID_SJEDISTA,NAZIV_SJEDISTA, LOKACIJA_SJEDISTA, KONTAKT)

    if(unos==2):
        print("Promijeni podatke o sjedistu")
        ID_SJEDISTA = int(input("Unesite ID:"))
        NAZIV_SJEDISTA = input("Unesite naziv sjedista:")
        LOKACIJA_SJEDISTA = input("Unesite lokaciju sjedista:")
        KONTAKT = int(input("Unesite kontakt: "))
        promjena_informacija=(ID_SJEDISTA,NAZIV_SJEDISTA,LOKACIJA_SJEDISTA, KONTAKT)

    if(unos==3):
        print("Brisi podatke o sjedistu.")
        ID_SJEDISTA = int(input("Unesite ID kako biste obrisali podatke o sjedistu:"))
        brisanje_informacija(ID_SJEDISTA)

    if(unos==4):
        print("Ispisi informacije o sjedistu")
        selektovanje_informacija()
    else:
        print("Greska.Probaj opet")
