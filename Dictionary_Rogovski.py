from module1 import *

riik_pealinn,pealinn_riik=loeson("riigid_pealinnd.txt")
while True:
    choice = int(input("0 - otse riik või pealinn\n1 - otse riik või pealinn\n"))
    if choice == 0:
        slovo = str(input("Sisesta riigi või pealinn: "))
        slovo.title
        if slovo.isalpha():
            finddict(slovo,riik_pealinn,pealinn_riik)
        else:
            print("Value error")
    elif choice == 1:
        riik_pealinn,pealinn_riik=loeson("riigid_pealinnd.txt")
        print(riik_pealinn)
        print(pealinn_riik)
    elif choice == 2:
        pass

        