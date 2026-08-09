def mergeSort(arr, s, e):
    
    if e - s +1 <= 1:
        return arr
    
    
    # The middle index of the array
    m = (s + e) // 2
    
    #sort the left half
    mergeSort(arr, s, m)
    
    #sort the right half
    mergeSort(arr, m+1, e)
    
    # merge sorted halfs
    merge(arr, s, m, e)
    
    return arr

# merge in-place
def merge(arr, s, m, e):
    
    L = arr[s: m+1]
    R = arr[m+1:e+1]
    
    i=0 # index for L
    j=0 # index for R
    k = s # index for arr, which is the start
    
    # merge the two sorted halfs into original array
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
            
        k += 1
        
    # One of the halfs will have elements remaing
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k +=1
        
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1
        
def main():
    
    arr = [5, 2, 9, 1, 3]
    mergeSort(arr, 0, len(arr) - 1)
    print(arr)


if __name__ == '__main__':
    
    main()