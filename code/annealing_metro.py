import numpy as np 
import matplotlib.pyplot as plt 
import scipy as sc 
#import map 


if __name__=="__main__":
    D=np.zeros((6,6))
    #PARIS 1, NANCY 2, STRASBOURG 3, MULHOUSE 4, BESANCON 5, DIJON 6
    #for i in range(5):
    #    for j in range(5):
    #        D[i,j]=np.sqrt((lons[i]-lons[j])**2+(lats[i]+lats[j])**2)
    D[0,1]=312;D[0,2]=445;D[0,3]=440;D[0,4]=365;D[0,5]=290
    #D[0,1]=815;D[0,2]=757;D[0,3]=850;D[0,4]=992;D[0,5]=1105 #Test remplacement Paris par Berlin 
    D[1,2]=133;D[1,3]=161;D[1,4]=184;D[1,5]=191
    D[2,3]=102;D[2,4]=227;D[2,5]=282
    D[3,4]=130;D[3,5]=204
    D[4,5]=83
    DD=np.transpose(D)+D
    T=np.arange(1,7,dtype=int)-1

    def facto(n):
        if n == 0 :
            return 1 
        else:
            return n*facto(n-1)

    def permutation(T,j,k):
        TT = T.copy()
        a=0;b=0
        a=TT[j];b=TT[k];TT[j]=b;TT[k]=a
        return TT

    def KM(TT):
        DT=np.zeros(6,dtype=int)
        KM=0
        for i in range(5):
            DT[i]=DD[TT[i],TT[i+1]]
            KM=DT[i]+KM
        return KM

    def generate_permutations(A,k, result): #Heap algorithm 
        if k == 1:
             result.append(list(A))
        else:
            generate_permutations(A,k - 1, result)
            for i in range(k - 1):
                if k % 2 == 0:
                    A[i], A[k-1] = A[k-1], A[i]
                else:
                    A[0], A[k-1] = A[k-1], A[0]
                generate_permutations(A, k - 1, result)

    liste=[]
    liste2=[]
    distance=[]
    generate_permutations(T,len(T),liste)

    for i in range(0,len(liste)):
        distance.append(KM(liste[i]))
        index=np.argmin(distance)
    print(distance[index],liste[index])


    #for i in range(1,len(liste)):
    #    if KM(liste[i]) < c: 
    #        c=KM(liste[i])
    #        liste2.append(liste[i])
    #    else: c=c;liste2.append(liste2)
        
    def random(T):
        p=int(np.random.rand()*6)
        m=int(np.random.rand()*6)
        TT=permutation(T,p,m)
        cc=KM(TT)
        return TT,cc
    distances=[]
    for j in range(100):   
        for i in range(10):
            F=0.003
            c=KM(T)
            TT,cc=random(T)
            if cc<c : 
                T=TT
            else :
                pc2 = np.exp(-F*cc)
                f = np.random.binomial(1,pc2)
                if f == 1 :
                    T=TT
        distances.append(c)
    ind = np.argmin(np.array(distances))
    print('Minimal: ', distances[ind])
    print('Average: ', np.mean(np.array(distances)))
        

    #print(TT,c)



    #Np=0 #nombre de permuations principales 
    #Np2=0 #nombre de sous-permutations 
    #iii=jjj=0
    #TT1=np.zeros((1,4),dtype=int)

    #for i in range(3): #boucle for des permutations principales (le zero du début va jusque la position de la dernière ville)
    #    TT1,ii,jj=permutation(T,i,i+1)
    #    liste.append(TT1) #permutation principale
    #    print(TT1,i,KM(TT1)[0])
    #    Np=Np+1 
    #    if KM(TT1)[0]<=compare:
    #        compare=KM(TT1)[0] #On garde en mémoire la permutation seulement si elle est pertinante (plus courte)
    #    if i >= 1 : #à partir de la position 2 du zeros on démarre les sous-permutations
    #        while Np2<=facto(i+2): #Tant que le nombre de sous permutations n'est pas égal au nombre de sous-permut on continu de tester
    #            j=np.arange(i+1) # Indices des sous-permutations possibles. 
    #            for p in range(i):
    #                TT1,ii,jj=permutation(TT1,j[p],j[p+1])
    #                print(TT1,i,KM(TT1)[0])
    #                liste.append(TT1)
    #                #print(TT1,KM(TT1)[0])
    #                Np2=Np2+1
    #                if KM(TT1)[0]<=compare:
    #                    compare=KM(TT1)[0]
    #                    iii=ii;jjj=jj
    #                if p+2 < i :
    #                    TT1,ii,jj=permutation(TT1,j[p],j[p+2])
    #                    liste.append(TT1)
    #                    Np2=Np2+1
    #                    if KM(TT1)[0]<=compare:
    #                        compare=KM(TT1)[0]
    #                        iii=ii;jjj=jj

    #print("Le chemin optimal prend",compare,"kms", " calculé en :",Np+Np2,"nombre d'essais"
    #    "  Il correspond à la permuation",iii,jjj) 
#
    #paris=[1,6.5];dijon=[6.5,2];besançon=[8.7,1.5];mulhouse=[11.5,3.1];strasbourg=[12.3,5.5];nancy=[9,6.9]
#
    #ville=np.zeros((6,2))
    #ville[0,:]=paris;ville[1,:]=dijon;ville[2,:]=besançon;ville[3,:]=mulhouse;ville[4,:]=strasbourg;ville[5,:]=nancy
    #plt.figure()
    #plt.plot(ville[:,0],ville[:,1])
    #plt.scatter(ville[:,0],ville[:,1])
    #plt.show()
    #print(liste)

