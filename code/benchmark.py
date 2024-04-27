import numpy as np
import matplotlib.pyplot as plt
from tools import *
from optimization import *
from heap import * 
import time 
import timeit
from analysis_beta import *

#N = np.array(range(2,30))



centers = [(0.25, 0.25), (0.5, 0.7), (0.75, 0.25), (0.75, 0.75)]  
side = 0.05


#plt.figure()
#plt.scatter(points[:,0],points[:,1],s=20)
##plt.show()
#temps=np.zeros(N-2)
#for i in range(2,N):
#    start=time.time()
#    allpermutations=generate_permutations(np.array(range(i)),i)
#    end=time.time()
#    temps[i-2]=end-start


step=5000
betas = np.array([5,12,1000])
  

beta=5
#times=np.zeros(np.size(N))
plt.figure()

#for j in range(2,28) :
#    points = clustered_cities(N[j], centers, side)
#    start=time.time()
#    current_itinerary=np.array(range(N[j]))
#    current_cost=np.zeros(step)
#   current_cost[0]=itinerary_cost(current_itinerary,points)  

N=10
points = clustered_cities(N, centers, side)
current_itinerary=np.array(range(N))
current_cost=np.zeros(step)
currentcost2=itinerary_cost(current_itinerary,points)  
start=time.time()

for i in range(1,step):
        num_cities = len(current_itinerary)
        new_itinerary = current_itinerary.copy()
        idx1, idx2 = np.random.choice(num_cities, 2, replace=False)     
        new_itinerary[idx1], new_itinerary[idx2] = new_itinerary[idx2], new_itinerary[idx1]       
        new_itinerary_cost=itinerary_cost(new_itinerary,points)         
        if new_itinerary_cost < currentcost2 or np.random.rand() < np.exp(-beta * (new_itinerary_cost - currentcost2)):         
                   current_itinerary= new_itinerary; currentcost2=new_itinerary_cost
        #else : current_cost[i]=current_cost[i-1]

end=time.time()  
times=end-start
print(times)

#plt.plot(N,times)
#plt.title("Time of calculations per number of points beta=5;step=5000")
#plt.xlabel("Number of points")
#plt.ylabel("Time of calculation in sec")
#plt.show()
#plt.figure()
#
#for beta in betas:    
#    print(f"Now doing {beta}")
#    current_itinerary=np.array(range(N))
#    current_cost=np.zeros(step)
#    current_cost[0]=itinerary_cost(current_itinerary,points)    
#    for i in range(1,step):
#        #best_itinerary, best_length = simulated_annealing(points,step,T0=10,alpha=0,cooling_schedule=0)
#        num_cities = len(current_itinerary)
#        new_itinerary = current_itinerary.copy()
#        idx1, idx2 = np.random.choice(num_cities, 2, replace=False)
#        new_itinerary[idx1], new_itinerary[idx2] = new_itinerary[idx2], new_itinerary[idx1]
#
#        new_itinerary_cost=itinerary_cost(new_itinerary,points)
#
#        if new_itinerary_cost < current_cost[i-1] or np.random.rand() < np.exp(-beta * (new_itinerary_cost - current_cost[i-1])):
#
#            current_itinerary= new_itinerary; current_cost[i]=new_itinerary_cost
#
#        else : current_cost[i]=current_cost[i-1]
#
#    plt.plot(current_cost[0::15], label = f"$\\beta$ = {beta}")
#plt.title("Behavior Metropolis algoritm depending on the temperature parameter")
#plt.xlabel("Number of steps of the Metropolis algorithm")
#plt.ylabel("Cost of the itinerary in function of step")
#plt.legend()
#plt.show()

#avg_cost=0 
#tot_cost=0
#coef=[]
#avg_cost_coef=[]
#nmetro=10
#steps=3000
#runs = 50
#current_itinerary_cost=np.zeros((6,steps))
#F= np.linspace(0.1, 1.1, 6)/10
#for p, F in enumerate(F):
#    current_itinerary=np.array(range(N))
#    tot_cost=0
#    for j in range(steps): #Nombre de step du metropolis 
#        #current_itinerary,current_itinerary_cost[p,j]=metropolis_step(F,current_itinerary,itinerary_cost,dont_permute=0)
#        num_cities = len(current_itinerary)
#        #RANDOM PERMUTATION
#        new_itinerary = current_itinerary.copy()
#        idx1, idx2 = np.random.choice(num_cities, 2, replace=False)
#        new_itinerary[idx1], new_itinerary[idx2] = new_itinerary[idx2], new_itinerary[idx1]
#        new_itinerary_cost=itinerary_cost(new_itinerary,points)
#
#        r = np.random.rand()
#
#        if new_itinerary_cost<current_itinerary_cost[p,j] : 
#            current_itinerary=new_itinerary
#            current_itinerary_cost[p,j]=new_itinerary_cost
#        else :
#            pc2 = np.exp(-p*(new_itinerary_cost-current_itinerary_cost[p,j]))
#            if pc2 < r : 
#                current_itinerary=new_itinerary
#                current_itinerary_cost[p,j]=new_itinerary_cost
#
#
#print(current_itinerary_cost[p,:])
#
#
#
#plt.figure()
##plt.plot(current_itinerary_cost[0,:])
##plt.plot(current_itinerary_cost[1,:])
##plt.plot(current_itinerary_cost[2,:])
#plt.plot(current_itinerary_cost[3,:])
##plt.plot(current_itinerary_cost[4,:])
##plt.plot(current_itinerary_cost[5,:])
##plt.xlabel("Beta values")
##plt.ylabel("Average cost of the best itinerary")
##plt.title("Metropolis_step=10000;number of Metropolis performed=10")
#plt.show()
##plt.figure()
##plt.plot(np.linspace(2,10,num=9),temps)
##plt.xlabel("Number of points/cities")
##plt.ylabel("Time to perform the Heap algoritm (in sec)")
##plt.title("Benchmark of the Heap algorithm")
##plt.show()
#
#allpermutations=generate_permutations(np.array(range(N)),N)
#cost_allitinerary=itinerary_cost_all(allpermutations,points) 
#best_itinerary_ind=np.argmin(cost_allitinerary)
#best_itinerary_cost=cost_allitinerary[best_itinerary_ind]
#best_itinerary=allpermutations[best_itinerary_ind]
##print(allpermutations,cost_allitinerary)
#print(best_itinerary,best_itinerary_cost)
##end=time.time()
##temps=end-start
##print(temps)
#
#

