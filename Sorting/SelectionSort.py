def selectionSort(arr):
    
    #iterate over the length of the list
    for i in range(len(arr)):
        
        #the minimum index is now equal to the current index
        #If the min_index is 1 (i=1) that means the current lowest
        #position is in the first index (i = 0)
        min_index = i
        
        #Iterate over the min_index + 1 to the length of the list
        for j in range(i+1, len(arr)):
            
            #if the element is smaller, swap
            if arr[min_index] > arr[j]:
                min_index = j
                
        arr[i], arr[min_index] = arr[min_index], arr[i]