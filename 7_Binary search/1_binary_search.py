arr = [2 , 5 , 7, 8 , 9 ,3 ,17]

def binary_search(arr , n , target):

    low = 0 
    high = n-1

    while low <= high :
        mid = (low+high) // 2 

        if arr[mid] == target :
            return mid
        elif target > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1

    return -1

if __name__ == "__main__":
    arr = [2 , 3 , 8 , 9 , 19 , 21 ,45]
    target = 8
    print(binary_search(arr , len(arr) , target))