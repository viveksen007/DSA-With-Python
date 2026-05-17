def binary_search(arr , low , high , target):
    if low > high :
        return -1
    
    mid = (low + high) // 2

    if arr[mid] == target :
        return mid
    elif target > arr[mid] :
       return binary_search(arr , mid+1 , high , target)
    else:
       return binary_search(arr , low , mid , target )

if __name__ == "__main__":
    arr = [2 , 3 , 8 , 9 , 19 , 21 ,45]
    target = 8
    print(binary_search(arr , 0 , 7 , target))