def binarySearch(arr, left, right, target):
    
    #base case
    if right >= left:
        
        mid = 1 + (right - left)/2
        
        if arr[mid] == x:
            return mid
        
        #If the target is smaller than the middle, the target is only present in the left subarray
        elif arr[mid] > x:
            return binarySearch(arr, left, mid-1, target)
        
        #Target is in the left subarray
        else:
            return binart(arr, mid+1, right, target)
    
    #target not in array
    else:
        return -1
    
    
        