#Traverse through the list with the first index as the 'max'
#Everything before the 'max' is sorted

#If we reach a value that is greater than the current 'max'
#switch places and there is now a new 'max' to be referenced


def insertionSort(arr):
    
    for i in range(1, len(arr)):
        
        key = arr[i]
        
        j = i-1
        while j>=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key