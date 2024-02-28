def generate_permutations(A,k, result):
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

array = [1, 2, 3, 4] 

result = []

generate_permutations(array ,len(array), result)

print(len(result))