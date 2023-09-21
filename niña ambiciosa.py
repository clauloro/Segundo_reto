def min_operations_to_zero_product(N, A):
    N_neg = sum(1 for x in A if x < 0)
    N_zero = A.count(0)
    
    if N_zero > 0:
        return 0
    elif N_neg % 2 == 0:
        return 2
    else:
        return 1

N = int(input())
A = list(map(int, input().split()))

resultado = min_operations_to_zero_product(N, A)
print(resultado)
