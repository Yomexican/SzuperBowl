class Donto:
    def __init__(self, adatsor):
        reszletek = adatsor.split(";")
        #adatmezők kialakítása
        self.ssz = reszletek[0]
        self.datum = reszletek[1]
        self.gyoztes = reszletek[2]
        self.eredmeny = reszletek[3]
        self.vesztes = reszletek[4]
        self.helyszin = [5]
        self.varosallam = [6]
        self.nezoszam = int(reszletek[7])

    def __str__(self):
        return f"{self.datum}, {self.helyszin}: {self.gyoztes} - {self.vesztes} ({self.eredmeny})"
    
    def pontkulombseg(self):
        reszletek = self.eredmeny.split('-')
        return int(reszletek[0]) - int(reszletek[1])



#0
print("Szuper Bowl döntőinek feldolgozása")

#1
finp = open("SuperBowl.txt", mode="rt", encoding="Utf8")
adatsorok = finp.read().split('\n')
finp.close()

dontok = []
for i in range(1, len(adatsorok)):
    if adatsorok[i] != "":
        donto = Donto(adatsorok[i])
        dontok.append(donto)


for item in dontok:
    print(item)
print("--------------------------------------------------------------------")
#programozási tételek
#összegzés tétele
#Határozza meg hogy a szuperbowl döntőket hány ember látogatta meg
sum = 0
for item in dontok :
    sum += item.nezoszam
print(f"sum = {sum}")
print("--------------------------------------------------------------------")

#átlag
#Határozza meg a látogatók átlagos számát
sum = 0
for item in dontok :
    sum += item.nezoszam
atlag = sum / len(dontok)
print(f"átlag = {atlag:.2f}")
print("--------------------------------------------------------------------")

#min max tétel
#min
#határozza meg hogy a döntők között milyen volt a legkisseb pontkülönbség
minpontkulombseg = dontok[0]
for item in dontok:
    if item.pontkulombseg() <minpontkulombseg.pontkulombseg():
        minpontkulombseg = item
print(f"main pontkülömbség: {minpontkulombseg.pontkulombseg()}")
print("--------------------------------------------------------------------")
#max
#határozza meg hogy a döntők során során elért legnagyobb pontkülönbséget
maxpontkulombseg = dontok[0]
for item in dontok:
    if item.pontkulombseg() > maxpontkulombseg.pontkulombseg():
        maxpontkulombseg = item
print(f"max pontkülömbség: {maxpontkulombseg.pontkulombseg()}")
print("--------------------------------------------------------------------")

#Határozza meg hogy a döntők során mi volt a maximális látogatottság
maxnezoszam = dontok[0]
for item in dontok:
    if item.nezoszam() > maxnezoszam.nezoszam():
        maxnezoszam = item
print(f"max nézőszám: {maxnezoszam.nezoszam()}")
print("--------------------------------------------------------------------")

#megszámlálás tétele
#Határozza meg hogy a dontok során hányszor nyert Pittsburg Steelers
dbPS = 0
for item in dontok:
    if item.gyoztes == "Pittsburg Steelers":
        dbPS += 1

        print(f"A 'Pittsburg Steelers'csapat {dbPS} győzött a döntők során" )
print("--------------------------------------------------------------------")



#eldöntés tétele
#legalább egy elem teljesíti a feltételt
#Határozza meg hogy volt-e olyan döntő ahol a két cspat közötti pontkülömbség meghalatta az 50-et
vanepontkulombseg50tobb = False
for item in dontok:
    if item.pontkulombseg() > 50:
        vanepontkulombseg50tobb = True
        break
if vanepontkulombseg50tobb:
    print("Igen volt megfelelő döntő")
else:
    print("nem volt megfelelő döntő")
print("--------------------------------------------------------------------")

#minden elem teljesíti 
#Határozza meg hogy a döntők során minden eggyes döntő a látogatottság meghalatta a 70000-et
mindennezoszam70etobb = True
for item in dontok:
    if not (item.nezoszam > 70000):
        mindennezoszam70etobb = False
        break
if mindennezoszam70etobb:
    print("Minden döntő teljesíti a feltételt")
else:
     print("Nem minden döntő teljesíti a feltételt")
print("--------------------------------------------------------------------")

#kiválasztás tétele
#!!!!!!!!!!!
#határozza meg az első olyan döntő ahol a nézőszám meghaladta a 100000-et
dontonezoszam100etobb = None
for item in dontok:
    if item.nezoszam >100000:
        dontonezoszam100etobb = item
        break
if dontonezoszam100etobb != None:
    print(f"Van ilyen döntő, amely nézőszáma: {dontonezoszam100etobb.nezoszam}")
else:
    print("Nincs megfelelő döntő")
print("--------------------------------------------------------------------")


#keresés tétele
#!!!!!!!!!!!!
#Keresse meg az első olyan döntőt amelyiknél a pontkülönbség a csapatok között 10
Indexponkul10 = None
for i in range(len(dontok)):
    if dontok[i].pontkulonbseg() == 10:
        Indexponkul10 = i
        break
if Indexponkul10 != None:
    print(f"Döntő :{dontok[Indexponkul10]}, NÉZŐSZÁM: {dontok[Indexponkul10].nezoszam}")
else:
    print("Nincs megfelelő döntő")
print("--------------------------------------------------------------------")   
#buborékos rendezés
#rendezze a döntőket pontok alapján csökkenő sorremdbe
for i in range(len(dontok)-1, 0, -1):
    for j in range(i):
        if dontok[j].pontkulombseg() < dontok[j+1].pontkulombseg():
            dontok[j], dontok[j+1] = dontok[j+1], dontok[j]

for item in dontok:
    print(item)