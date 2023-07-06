import sqlite3

connection=sqlite3.connect("trgovina.db")
cursor=connection.cursor()
sql_command="""
CREATE TABLE Kupci(
ID_KUPCA INTEGER PRIMARY KEY,
IME_KUPCA VARCHAR(50),
PREZIME_KUPCA VARCHAR(50),
JMBG_KUPCA INTEGER
);
"""
cursor.execute(sql_command)
connection.close()
from tabulate import tabulate
import sqlite3
connection=sqlite3.connect("trgovina.db")

def unos_informacija(ID_KUPCA, IME_KUPCA,PREZIME_KUPCA,JMBG_KUPCA):
    qry="INSERT INTO Kupci(ID_KUPCA, IME_KUPCA, PREZIME_KUPCA,JMBG_KUPCA)VALUES(?,?,?,?);"
    connection.execute(qry,(ID_KUPCA,IME_KUPCA,PREZIME_KUPCA,JMBG_KUPCA))
    connection.commit()
    print("Registrovali ste novog kupca")

def izmjena_informacija(ID_KUPCA, IME_KUPCA, PREZIME_KUPCA,JMBG_KUPCA):
    qry="UPDATE Kupci set ID_KUPCA=?, IME_KUPCA=?, PREZIME_KUPCA=?,JMBG_KUPCA=? WHERE ID_KUPCA=?;"
    connection.execute(qry,(ID_KUPCA, IME_KUPCA, PREZIME_KUPCA,JMBG_KUPCA))
    connection.commit()
    print("Podaci o kupcu su izmijenjeni")
    res=connection.cursor()
    qry="UPDATE Kupci set ID_KUPCA=?, IME_KUPCA=?, PREZIME_KUPCA=?,JMBG_KUPCA=? WHERE ID_KUPCA=?;"
    Kupci=(ID_KUPCA, IME_KUPCA, PREZIME_KUPCA,JMBG_KUPCA)
    res.execute(qry, Kupci)
    connection.commit()
    print("Uspjesno je izvrsena promjena")

def brisanje_informacije(ID_KUPCA):
    qry="DELETE FROM Kupci WHERE ID_KUPCA=?;"
    connection.execute(qry,(ID_KUPCA))
    connection.commit()
    print("Podaci su obrisani!!!")
    res=connection.cursor()
    qry="DELETE FROM Kupci WHERE ID_KUPCA=?"
    res=connection.cursor()
    izbrisi=(ID_KUPCA)
    res.execute(qry,izbrisi)
    connection.commit()
    print("Podaci su izbrisani")

def selektovanje_informacija():
    res=connection.cursor()
    qry="SELECT*FROM Kupci"
    res.execute(qry)
    rezultat=res.fetchall()
    print(tabulate(rezultat,headers=["ID_KUPCA", "IME_KUPCA", "PREZIME_KUPCA","JMBG_KUPCA"]))
    if res.rowcount<0:
        print("Nema podataka")
    else:
        for podaci in rezultat:
            print(podaci)
def prikaz_meni(connection):
    print("Prikazi opcije")
    print("1. Ubacivanje podataka")
    print("2. Selektovanje podataka")
    print("3. Izmjena podataka")
    print("4. Brisanje podataka")
    menu=input("Izaberi opciju:")
    if menu=="1":
        unos_informacija(connection)
    elif menu=="2":
        selektovanje_informacija(connection)
    elif menu=="3":
        izmjena_informacija(connection)
    elif menu=="4":
        brisanje_informacije(connection)
    else:
        print("Greska")
    if __name__=="__main__":
        while(True):
            prikaz_meni(connection)

