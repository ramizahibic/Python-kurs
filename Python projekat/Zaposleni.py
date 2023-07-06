import sqlite3
from datetime import datetime

connection=sqlite3.connect("trgovina.db")
cursor=connection.cursor()
sql_command="""
CREATE TABLE Zaposleni(
ID_ZAPOSLENOG INTEGER PRIMARY KEY,
IME_ZAPOSLENOG VARCHAR(50),
PREZIME_ZAPOSLENOG VARCHAR(50),
JMBG_ZAPOSLENOG INTEGER
);
"""
cursor.execute(sql_command)
connection.close()
from tabulate import tabulate
import sqlite3
connection=sqlite3.connect("trgovina.db")

def unos_informacija(ID_ZAPOSLENOG, IME_ZAPOSLENOG,PREZIME_ZAPOSLENOG,JMBG_ZAPOSLENOG):
    qry="INSERT INTO Zaposleni(ID_ZAPOSLENOG, IME_ZAPOSLENOG, PREZIME_ZAPOSLENOG,JMBG_ZAPOSLENOG)VALUES(?,?,?,?);"
    connection.execute(qry,(ID_ZAPOSLENOG,IME_ZAPOSLENOG,PREZIME_ZAPOSLENOG,JMBG_ZAPOSLENOG))
    connection.commit()
    print("Unijeli ste novog zaposlenika")

def izmjena_informacija(ID_ZAPOSLENOG, IME_ZAPOSLENOG, PREZIME_ZAPOSLENOG,JMBG_ZAPOSLENOG):
    qry="UPDATE Zaposleni set ID_ZAPOSLENOG=?, IME_ZAPOSLENOG=?, PREZIME_ZAPOSLENOG=?,JMBG_ZAPOSLENOG=? WHERE ID_ZAPOSLENOG=?;"
    connection.execute(qry,(ID_ZAPOSLENOG, IME_ZAPOSLENOG, PREZIME_ZAPOSLENOG,JMBG_ZAPOSLENOG))
    connection.commit()
    print("Podaci o zaposlenom su izmijenjeni")
    res=connection.cursor()
    qry="UPDATE Zaposleni set ID_ZAPOSLENOG=?, IME_ZAPOSLENOG=?, PREZIME_ZAPOSLENOG=?,JMBG_ZAPOSLENOG=? WHERE ID_ZAPOSLENOG=?;"
    Zaposleni=(ID_ZAPOSLENOG, IME_ZAPOSLENOG, PREZIME_ZAPOSLENOG,JMBG_ZAPOSLENOG)
    res.execute(qry, Zaposleni)
    connection.commit()
    print("Uspjesno je izvrsena promjena")

def brisanje_informacije(ID_Zaposlenog):
    qry="DELETE FROM Zaposleni WHERE ID_Zaposlenog=?;"
    connection.execute(qry,(ID_Zaposlenog))
    connection.commit()
    print("Podaci su obrisani!!!")
    res=connection.cursor()
    qry="DELETE FROM Zaposleni WHERE ID_Zaposlenog=?"
    res=connection.cursor()
    izbrisi=(ID_Zaposlenog)
    res.execute(qry,izbrisi)
    connection.commit()
    print("Podaci su izbrisani")

def selektovanje_informacija():
    res=connection.cursor()
    qry="SELECT*FROM Zaposleni"
    res.execute(qry)
    rezultat=res.fetchall()
    print(tabulate(rezultat,headers=["ID_ZAPOSLENOG", "IME_ZAPOSLENOG", "PREZIME_ZAPOSLENOG","JMBG_ZAPOSLENOG"]))
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






