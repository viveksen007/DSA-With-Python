# higher bound = smallest index such  that arr[index] > n


def upper_Bound(arr, n , target):
    low = 0
    high = n-1
    ans = n

    

    while low <=high :
        
        mid = (low+high) // 2

        if arr[mid] > target :
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

if __name__ == "__main__":
    arr = [ 2, 3 , 5, 8 , 9 , 11 ,  15 , 18]
    target = 6
    print(upper_Bound(arr , len(arr) , target))

