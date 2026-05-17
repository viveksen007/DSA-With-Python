def Search_insert (arr , n , target):

    low = 0
    high = n-1
    ans = n

    while low <= high :

        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] >= target:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

if __name__ == "__main__":
    arr = [1 , 2, 4, 7]
    target = 3
    print(Search_insert(arr, len(arr) , target))
