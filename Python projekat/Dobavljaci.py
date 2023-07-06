import sqlite3

connection=sqlite3.connect("trgovina.db")
cursor=connection.cursor()
sql_command="""
CREATE TABLE Dobavljaci(
ID_DOBAVLJACA INTEGER PRIMARY KEY,
NAZIV_DOBAVLJACA VARCHAR(50),
ADRESA VARCHAR(50),
BROJ_TELEFONA INTEGER
);
"""
cursor.execute(sql_command)
connection.close()
from tabulate import tabulate
import sqlite3
connection=sqlite3.connect("trgovina.db")

def unos_informacija(ID_DOBAVLJACA, NAZIV_DOBAVLJACA,ADRESA,BROJ_TELEFONA):
    qry="INSERT INTO Dobavljaci(ID_DOBAVLJACA, NAZIV_DOBAVLJACA, ADRESA, BROJ_TELEFONA)VALUES(?,?,?,?);"
    connection.execute(qry,(ID_DOBAVLJACA, NAZIV_DOBAVLJACA,ADRESA,BROJ_TELEFONA))
    connection.commit()
    print("Unijeli ste novog dobavljaca")

def izmjena_informacija(ID_DOBAVLJACA, NAZIV_DOBAVLJACA,ADRESA,BROJ_TELEFONA):
    qry="UPDATE Dobavljaci set ID_DOBAVLJACA=?, NAZIV_DOBAVLJACA=?, ADRESA=?, BROJ_TELEFONA=? WHERE ID_DOBAVLJACA=?;"
    connection.execute(qry,(ID_DOBAVLJACA, NAZIV_DOBAVLJACA,ADRESA,BROJ_TELEFONA))
    connection.commit()
    print("Podaci o dobavljacu su izmijenjeni")
    res=connection.cursor()
    qry="UPDATE Dobavljaci set ID_DOBAVLJACA=?, NAZIV_DOBAVLJACA=?, ADRESA=?,BROJ_TELEFONA=? WHERE ID_DOBAVLJACA=?;"
    Dobavljaci=(ID_DOBAVLJACA, NAZIV_DOBAVLJACA,ADRESA,BROJ_TELEFONA)
    res.execute(qry, Dobavljaci)
    connection.commit()
    print("Uspjesno je izvrsena promjena")

def brisanje_informacije(ID_DOBAVLJACA):
    qry="DELETE FROM Dobavljaci WHERE ID_DOBAVLJACA=?;"
    connection.execute(qry,(ID_DOBAVLJACA))
    connection.commit()
    print("Podaci su obrisani!!!")
    res=connection.cursor()
    qry="DELETE FROM Dobavljaci WHERE ID_DOBAVLJACA=?"
    res=connection.cursor()
    izbrisi=(ID_DOBAVLJACA)
    res.execute(qry,izbrisi)
    connection.commit()
    print("Podaci su izbrisani")

def selektovanje_informacija():
    res=connection.cursor()
    qry="SELECT*FROM Dobavljaci"
    res.execute(qry)
    rezultat=res.fetchall()
    print(tabulate(rezultat,headers=["ID_DOBAVLJACA", "NAZIV_DOBAVLJACA", "ADRESA","BROJ_TELEFONA"]))
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