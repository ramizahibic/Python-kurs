import sqlite3

connection=sqlite3.connect("trgovina.db")
cursor=connection.cursor()
sql_command="""
CREATE TABLE Proizvodi(
ID_PROIZVODA INTEGER PRIMARY KEY,
NAZIV_PROIZVODA VARCHAR(50),
KOLICINA_PROIZVODA INTEGER,
CIJENA INTEGER
);
"""
cursor.execute(sql_command)
connection.close()
from tabulate import tabulate
import sqlite3
connection=sqlite3.connect("trgovina.db")

def unos_informacija(ID_PROIZVODA, NAZIV_PROIZVODA,KOLICINA_PROIZVODA,CIJENA):
    qry="INSERT INTO Kupci(ID_PROIZVODA, NAZIV_PROIZVODA, KOLICINA_PROIZVODA, CIJENA)VALUES(?,?,?,?);"
    connection.execute(qry,(ID_PROIZVODA, NAZIV_PROIZVODA, KOLICINA_PROIZVODA, CIJENA))
    connection.commit()
    print("Registrovali ste novi proizvod")

def izmjena_informacija(ID_PROIZVODA, NAZIV_PROIZVODA, KOLICINA_PROIZVODA, CIJENA):
    qry="UPDATE Proizvodi set ID_PROIZVODA=?, NAZIV_PROIZVODA=?, KOLICINA_PROIZVODA=?,CIJENA=? WHERE ID_PROIZVODA=?;"
    connection.execute(qry,(ID_PROIZVODA, NAZIV_PROIZVODA, KOLICINA_PROIZVODA, CIJENA))
    connection.commit()
    print("Podaci o proizvodu su izmijenjeni")
    res=connection.cursor()
    qry="UPDATE Proizvodi set ID_PROIZVODA=?, NAZIV_PROIZVODA=?, KOLICINA_PROIZVODA=?,CIJENA=? WHERE ID_PROIZVODA=?;"
    Proizvodi=(ID_PROIZVODA, NAZIV_PROIZVODA, KOLICINA_PROIZVODA, CIJENA)
    res.execute(qry, Proizvodi)
    connection.commit()
    print("Uspjesno je izvrsena promjena")

def brisanje_informacije(ID_PROIZVODA):
    qry="DELETE FROM Proizvodi WHERE ID_PROIZVODA=?;"
    connection.execute(qry,(ID_PROIZVODA))
    connection.commit()
    print("Podaci su obrisani!!!")
    res=connection.cursor()
    qry="DELETE FROM Proizvodi WHERE ID_PROIZVODA=?"
    res=connection.cursor()
    izbrisi=(ID_PROIZVODA)
    res.execute(qry,izbrisi)
    connection.commit()
    print("Podaci su izbrisani")

def selektovanje_informacija():
    res=connection.cursor()
    qry="SELECT*FROM Proizvodi"
    res.execute(qry)
    rezultat=res.fetchall()
    print(tabulate(rezultat,headers=["ID_PROIZVODA", "NAZIV_PROIZVODA", "KOLCINA_PROIZVODA","CIJENA"]))
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