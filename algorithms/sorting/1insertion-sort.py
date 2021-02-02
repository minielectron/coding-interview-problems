import numpy as np

arr = np.array([2,5,3,7,9,8,0])

def sort(a):
    j = 0
    size = len(a)
    while(j < size ):
        key = a[j]
        i = j - 1
        while i >= 0 and a[i] > key:
            a[i + 1] = a [i]
            i = i - 1            
        j= j + 1
        a[i+1] = key
    return a

print(sort(arr))


# Worst case: When array is reverse sorted - Time complexity will be O(n^2)
# Best case: When array is already sorted - Time complexity will be O(n)