# Lower bound -> smallest index such that arr[index] >= n

def Lower_bound(arr , n , target):
    low = 0 
    high = n-1 
    ans = n

    while low <= high :
        
        mid = (low + high) // 2

        if arr[mid] >= target :
            ans = mid 
            high = mid - 1
        else :
            low = mid + 1 
    return ans 

if __name__ == "__main__":
    arr = [2 , 3 , 8 , 9 , 15 , 17]
    target = 10
    print(Lower_bound(arr, len(arr) , target))