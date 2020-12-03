def mutateTheArray(n, a):
    b = list(a)
    for i in range(n):
        low = 0 if i - 1 < 0 else a[i - 1]
        high = 0 if i + 1 > n - 1 else a[i + 1]
        b[i] = low + a[i] + high
        
    return b

print(mutateTheArray(5, [4, 0, 1, -2, 3]))




# Output:
# [4, 5, 4, 5, 3]
# Expected Output:
# [4, 5, -1, 2, 1]