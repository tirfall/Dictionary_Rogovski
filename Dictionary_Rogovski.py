from module1 import *

riik_pealinn,pealinn_riik=loeson("riigid_pealinnd.txt")
while True:
    choice = int(input("0 - otse riik või pealinn\n1 - loefail\n2 - lisa riik ja pealinn\n3 - parandada\n4 - test\n5 - gtts\n6 - vaata sonastikud\n7 - salvestamine\n8 - exit\n"))
    if choice == 0:
        slovo = str(input("Sisesta riigi või pealinn: "))
        slovo.title
        if slovo.isalpha():
            finddict(slovo,riik_pealinn,pealinn_riik)
        else:
            print("Value error")
    elif choice == 1:
        riik_pealinn,pealinn_riik=loeson("riigid_pealinnd.txt")
    elif choice == 2:
        lisriik(riik_pealinn,pealinn_riik)
    elif choice == 3:
        parandada(riik_pealinn,pealinn_riik)
    elif choice == 4:
        test(riik_pealinn)
    elif choice == 5:
        heli(riik_pealinn)
    elif choice == 6:
        print(riik_pealinn)
    elif choice == 7:
        salvestamine("riigid_pealinnd.txt",riik_pealinn)
    elif choice == 8:
        break
        