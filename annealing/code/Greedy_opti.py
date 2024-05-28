import numpy as np
import matplotlib.pyplot as plt
from tools import *
from optimization import *
from heap import * 
import time 
import timeit
from analysis_beta import *


N=10
centers = [(0.25, 0.25), (0.5, 0.7), (0.75, 0.25), (0.75, 0.75)]  
side = 0.05
points = clustered_cities(N, centers, side)
#allpermutations=generate_permutations(np.array(range(N)),N)
#cost_allitinerary=itinerary_cost_all(allpermutations,points) 
#best_itinerary_ind=np.argmin(cost_allitinerary)
#best_itinerary_cost=cost_allitinerary[best_itinerary_ind]
#best_itinerary=allpermutations[best_itinerary_ind]
#print(best_itinerary,best_itinerary_cost)
start=time.time()
result=[]
best_cost=0
best_itinerary=[]
best_cost=heaps_algorithm_cost(np.array(range(N)),N,result,itinerary_cost,points, previous_cost=None)
end=time.time()
timee=end-start
print(timee)



