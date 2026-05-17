# floor -> largest no. in array <= X 
# Ceil -> smallest no. in array >= x

def floor_ceil (arr , n , target):

    low = 0
    high = n
    res1 = 0
    res2 = n

    while low <= high:

        mid = (low + high) // 2

        if arr[mid] <= target:
            res1 = mid
            low = mid + 1
        elif arr[mid] >= target:
            res2 = mid
            high = mid - 1

    return res1 , res2

if __name__ == "__main__":
    arr = [10  , 15 , 20 , 30 , 40 , 50]
    target = 25
    print(floor_ceil(arr, len(arr) , target))


           

            
