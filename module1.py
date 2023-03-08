import random
import os
from gtts import gTTS


def finddict(slovo,ridict,pedict):
    loeson
    x = ridict.get(slovo)
    if x == None:
        y =  pedict.get(slovo)
        print(y)
        if y == None:
            jahei = input("Seda pealinn/riik ei ole sõnastikus.\nKas sa tahad lisa seda riik/pealinn?").lower()
            if jahei == "jah":
                lisriik(ridict,pedict)
            else:
                pass
    else:
        print(x)

def loeson(f:str):
    riik_pealinn={}
    pealinn_riik={}
    file = open (f, 'r', encoding="utf-8")
    for line in file:
        k, v=line.strip().split('-')
        riik_pealinn[k] = v
        pealinn_riik[v] = k
    file.close()
    return riik_pealinn,pealinn_riik

def lisriik(ridict,pedict):
    riik = input("Sisesta riik: ").title()
    pealinn = input ("Sisesta pealinn: ").title()
    ridict.update({riik:pealinn})
    pedict.update({pealinn:riik})

def parandada(ridict,pedict):
    riik = input("Sisesta riik mis sa tahab parandada: ").title()
    pealinn = input ("Sisesta pealinn mis sa tahab parandada: ").title()
    riik1 = input("Sisesta õige riik: ").title()
    pealinn1 = input ("Sisesta õige pealinn: ").title()
    del ridict[riik]
    ridict.update({riik1:pealinn1})
    del pedict[pealinn]
    pedict.update({pealinn1:riik1})

def test (ridict):
    goodans=0
    badans=0
    anstest=int(input("Kui palju küsimused sa tahad? "))
    kluch = list(ridict.keys())
    means = list(ridict.values())
    for j in range(anstest):
        x = random.choice([kluch,means])
        word = random.choice(x)
        ind = x.index(word)
        print(word)
        slovo = input("Sisesta vastus: ").title()
        if slovo in kluch or slovo in means:
            if x == kluch:
                spisok = means
                indans = spisok.index(slovo)
            elif x == means:
                spisok = kluch
                indans = spisok.index(slovo)
            if indans == ind:
                goodans += 1
                print("Õige vastus")
            elif indans != ind:
                badans += 1
                print("Vale vastus")
        else:
            badans += 1
            print("Vale vastus1")
    print(goodans,"Õiged vastused")
    print(badans,"Valed vastused")
    finalscore=round(goodans/anstest*100,2)
    print(finalscore, "%")

def heli(ridict):
    n = input("Sisesta riik:")
    text = str(ridict.get(n))
    keel='en'
    gTTS(text=text, lang=keel, slow=False).save("heli.mp3")
    os.system("heli.mp3")

def salvestamine(f:str,ridict):
    f = open(f, "w", encoding="utf-8-sig")
    for key, value in ridict.items():
        f.write(f'{key}-{value}\n')
    f.close