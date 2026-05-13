# selection sorting 

def selection_sorting(arr):

    n = len(arr)

    for left in range(0, n):
        min = left
        for right in range(left , n):
            if arr[right] < arr[min]:
                arr[min] , arr[right] = arr[right] , arr[min]
    
    return arr
    
if __name__ == "__main__":
    arr = [13 , 46 , 24 , 20 , 52 , 9]
    print(selection_sorting(arr))