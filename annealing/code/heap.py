import numpy as np

def heaps_algorithm(A,k,result):
    if k == 1:
        result.append(list(A))
    else:
        heaps_algorithm(A,k - 1, result)
        for i in range(k - 1):
            if k % 2 == 0:
                A[i], A[k-1] = A[k-1], A[i]
            else:
                A[0], A[k-1] = A[k-1], A[0]
            heaps_algorithm(A, k - 1, result)


def heaps_algorithm_cost(A,k,result,cost_function,cities):
    if k == 1 :
        result.append(list(A))
    else:
        heaps_algorithm(A,k - 1, result)
        for i in range(k - 1):
            if k % 2 == 0:
                A[i], A[k-1] = A[k-1], A[i]
            else:
                A[0], A[k-1] = A[k-1], A[0]
            heaps_algorithm(A, k - 1, result)


def heaps_algorithm_cost(A, k, result, cost_function, cities, previous_cost=None):
    if k == 1:
        current_cost = cost_function(A, cities)
        if previous_cost is None or current_cost < previous_cost:
            result.clear()
            result.append(list(A))
            return current_cost
        else:
            return previous_cost
    else:
        previous_cost = heaps_algorithm_cost(A, k - 1, result, cost_function, cities, previous_cost)
        for i in range(k - 1):
            if k % 2 == 0:
                A[i], A[k-1] = A[k-1], A[i]
            else:
                A[0], A[k-1] = A[k-1], A[0]
            previous_cost = heaps_algorithm_cost(A, k - 1, result, cost_function, cities, previous_cost)
        return previous_cost

def generate_permutations(A,k):
    result = []
    heaps_algorithm(A,k,result)
    return np.array(result)


if __name__ == '__main__':
    # Just an example
    array = [1, 2, 3, 4]
    permutations = generate_permutations(array,len(array)-1)
    print('Voici toutes les permutations: \n')
    for permutation in permutations:
        print(permutation)
    print(f'Number of permutations is {len(permutations)}, and type of array is {type(permutations)}')