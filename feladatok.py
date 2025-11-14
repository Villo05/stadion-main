from Stadion import Stadion
from datetime import datetime

stadionok_lista=[]

def beolvasas():
    b = open("stadionok.txt", "r", encoding="UTF-8")
    b.readline()
    sorok_lista=b.readlines()
    print(sorok_lista)
    print(type(sorok_lista))
    b.close()

    i=0
    while i<len(sorok_lista):
        sor=sorok_lista[i].strip().split(";")
        stadion=Stadion(sor[0],sor[1],int(sor[2]),sor[3],sor[4])
        stadionok_lista.append(stadion)
        i+=1



"""
1. Összesen hány stadion van New Yorkban? 

2. Mennyi az összes csapatszám? 

3. listázd ki azokat a stadionokat, amelyekben  1900.01.01 előtt volt az első mérkőzésük!

4. Hány olyan stadion van, amelyben 2000 óta nem volt mérkőzés? 

5. Összesen hány csapat játszott Buffalo - ban?
"""

def elso_feladat():
    i=0
    db=0
    while i<len(stadionok_lista):
        print(stadionok_lista[i])
        if stadionok_lista[i].varos=="New York":
            db+=1
        i+=1
    return db


def masodik_feladat():
    i=0
    osszesen=0
    while i<len(stadionok_lista):
        osszesen += stadionok_lista[i].csap_szama
        i+=1
    return osszesen


def harmadik_feladat():
    i=0
    elott=datetime(1900,1,1)
    korabbi=[]
    while i<len(stadionok_lista):
        sor = stadionok_lista[i]
        utolso = datetime.strptime(sor.elso_m, "%Y-%m-%d")
        if utolso < elott:
            korabbi.append(sor.stadion_nev)
        i += 1
    return korabbi


def negyedik_feladat():
    i=0
    utan=datetime(2000,1,1)
    db=0
    while i<len(stadionok_lista):
        stadionok = stadionok_lista[i]
        utolso = datetime.strptime(stadionok.utolso_m, "%Y-%m-%d")
        if utolso < utan:
            db+=1
        i += 1
    return db


def otodik_feladat():
    i=0
    db=0
    while i<len(stadionok_lista):
        print(stadionok_lista[i])
        if stadionok_lista[i].varos=="Buffalo":
            db+=1
        i+=1
    return db




            







