# soit a et b deux ensembles a = (1,2,3...) b =( ... )
a=(3,1,7,9)
b=(2,4,1,9,3)

# Fonction qui verifie si x appartient à l'ensemble a
def existInSet(x,a):
    boolean = False
    for i in a:
        if i == x:
            boolean  = True
    return boolean

c=[]
somme=0
for i in a:
    if (not existInSet(i,b)):
        c.append(i)
for i in b:
    if ((not existInSet(i,a)) and (not existInSet(i,c))):
        c.append(i)
print(sum(c))   