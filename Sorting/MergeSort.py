def merge(arr, left, middle, right):
    
    n1 = m - 1 + 1
    n2 = r - m
    
    L = [0] * n1
    R = [0] * n2
    
    for i in range(n1):
        L[i] = arr[l + i]
    
    for i in range(n2):
        R[i] = arr[m+1+i]
    
    #Initial index of first subarray
    i = 0
    #Initial index of second subarray
    j = 0
    #Initial index of merged subarray
    k = l
    
    #merge temp arrays back into arr[l..r]
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    
    
    #Copy remaining elements of L and R, if any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
    
#l = left index, r = right index of subarrays to be sorted
def mergeSort(arr, l, r):
    if l < r:
        
        m = (l +(r-1))/2
        
        #sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)