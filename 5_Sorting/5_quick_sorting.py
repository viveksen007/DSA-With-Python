# quick sorting 
def partition(arr , low , high):
    pivot = arr[low]
    i = low
    j = high

    while i <= j:

        while i <= high and arr[i] <= pivot:
            i += 1

        while j >= low and arr[j] > pivot :
            j -= 1

        if i < j:
            arr[i] , arr[j] = arr[j] , arr[i]
    
    arr[low] , arr[j] = arr[j] , arr[low]
    return j 

def quick_sorting(arr , low , high):

    if low < high :

        pindex = partition(arr , low , high)
        quick_sorting(arr , low , pindex-1)
        quick_sorting(arr , pindex+1 , high)

if __name__ == "__main__":
    arr = [13 , 46 , 24 , 20 , 52 , 9]
    print(quick_sorting(arr , 0 , len(arr)-1))
    print(arr)