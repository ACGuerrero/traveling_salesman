from memory_profiler import profile
from benchmark import *
from tools import *
from optimization import *
from heap import * 

@profile
def my_algorithm():
    import numpy as np
    import matplotlib.pyplot as plt
    N = 9
    centers = [(0.25, 0.25), (0.5, 0.7), (0.75, 0.25), (0.75, 0.75)]  
    side = 0.05
    points = clustered_cities(N, centers, side)

    plt.figure()
    plt.scatter(points[:,0],points[:,1],s=20)
    #plt.show()

    allpermutations=generate_permutations(np.array(range(N)),N)
    cost_allitinerary=itinerary_cost_all(allpermutations,points) 
    best_itinerary_ind=np.argmin(cost_allitinerary)
    best_itinerary_cost=cost_allitinerary[best_itinerary_ind]
    best_itinerary=allpermutations[best_itinerary_ind]
    #print(allpermutations,cost_allitinerary)
    print(best_itinerary,best_itinerary_cost)

