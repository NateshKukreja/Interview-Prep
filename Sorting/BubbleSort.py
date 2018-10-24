def bubbleSort(arr):
    
    #Iterate through all the elements
    for i in range(len(arr)):
        
        #Iterate through the element that are NOT in place
        #The last elements will be in place
        for j in range(0, len(arr)-i-1):
    
            #swap if the element is greater than the next
            #element
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 