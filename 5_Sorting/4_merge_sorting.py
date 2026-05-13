# Merge sorting -> divide & merge 

def merge(arr , low , mid , high ):
    
    temp = []
    left = low
    right = mid + 1 
    n = len(arr)

    while left <= mid and right <= high:

        if arr[left]  <= arr[right]:
            temp.append(arr[left])
            left += 1
        else : 
            temp.append(arr[right])
            right += 1

    while left <= mid:
        temp.append(arr[left])
        left += 1

    while right <= high:
        temp.append(arr[right])
        right += 1

    for i in range (low , high+1):
        arr[i] = temp[i-low]
        

def merge_sorting(arr , low , high):


    if low >= high :
        return 
    
    mid = int((low + high)/2)

    merge_sorting(arr , low , mid)
    merge_sorting(arr , mid + 1 , high)
    merge(arr , low , mid , high)

if __name__ == "__main__":
    arr = [13 , 46 , 24 , 20 , 52 , 9]
    merge_sorting(arr , 0 , 5)
    print(arr)