def finddict(slovo,riik_pealinn,pealinn_riik):
    loeson
    x = riik_pealinn.get(slovo)
    if x == None:
        y =  pealinn_riik.get(slovo)
        print(y)
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