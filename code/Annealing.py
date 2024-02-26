import numpy as np 
import matplotlib.pyplot as plt 
import scipy as sc 

D=np.zeros((6,6))
#PARIS 1, NANCY 2, STRASBOURG 3, MULHOUSE 4, BESANCON 5, DIJON 6

#D[0,1]=312;D[0,2]=445;D[0,3]=440;D[0,4]=365;D[0,5]=290
D[0,1]=815;D[0,2]=757;D[0,3]=850;D[0,4]=992;D[0,5]=1105 #Test remplacement Paris par Berlin 
D[1,2]=133;D[1,3]=161;D[1,4]=184;D[1,5]=191
D[2,3]=102;D[2,4]=227;D[2,5]=282
D[3,4]=130;D[3,5]=204
D[4,5]=83
DD=np.transpose(D)+D
T=np.arange(1,7,dtype=int)-1
TT=np.zeros((2,6),dtype=int) #Tableau valeur ordre 
TT[0,:]=T
TT[1,:]=T
print(TT)

def facto(n):
    if n == 0 :
        return 1 
    else:
        return n*facto(n-1)

def permutation(TT,j,k):
    a=0;b=0
    a=TT[0,j];b=TT[0,k];TT[0,j]=b;TT[0,k]=a
    return TT,j,k

def KM(TT):
    DT=np.zeros(6,dtype=int)
    KM=0
    for i in range(5):
        DT[i]=DD[TT[0,i],TT[0,i+1]]
        KM=DT[i]+KM
    return KM,TT

compare=KM(TT)[0]
#print(compare)
Np=0 #nombre de permuations principales 
Np2=0 #nombre de sous-permutations 
iii=jjj=0
TT1=np.zeros((2,6),dtype=int)
for i in range(5): #boucle for des permutations principales (le zero du début va jusque la position de la dernière ville)
    TT1,ii,jj=permutation(TT,i,i+1) #permutation principale
    #print(TT1,i,KM(TT1)[0])
    Np=Np+1 
    if KM(TT1)[0]<=compare:
        compare=KM(TT1)[0] #On garde en mémoire la permutation seulement si elle est pertinante (plus courte)
    if i >= 1 : #à partir de la position 2 du zeros on démarre les sous-permutations
        while Np2<=facto(i+2): #Tant que le nombre de sous permutations n'est pas égal au nombre de sous-permut on continu de tester
            j=np.arange(i+1) # Indices des sous-permutations possibles. 
            for p in range(i):
                TT1,ii,jj=permutation(TT1,j[p],j[p+1])
                #print(TT1,KM(TT1)[0])
                Np2=Np2+1
                if KM(TT1)[0]<=compare:
                    compare=KM(TT1)[0]
                    iii=ii;jjj=jj
                if p+2 < i :
                    TT1,ii,jj=permutation(TT1,j[p],j[p+2])
                    Np2=Np2+1
                    if KM(TT1)[0]<=compare:
                        compare=KM(TT1)[0]
                        iii=ii;jjj=jj

print("Le chemin optimal prend",compare,"kms", " calculé en :",Np+Np2,"nombre d'essais"
      "  Il correspond à la permuation",iii,jjj) 

paris=[1,6.5];dijon=[6.5,2];besançon=[8.7,1.5];mulhouse=[11.5,3.1];strasbourg=[12.3,5.5];nancy=[9,6.9]

ville=np.zeros((6,2))
ville[0,:]=paris;ville[1,:]=dijon;ville[2,:]=besançon;ville[3,:]=mulhouse;ville[4,:]=strasbourg;ville[5,:]=nancy
plt.figure()
plt.plot(ville[:,0],ville[:,1])
plt.scatter(ville[:,0],ville[:,1])
plt.show()