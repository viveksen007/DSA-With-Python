# insertion sorting 

def insertion_sorting(arr):

    n = len(arr)

    for i in range(0 , n):
        j = i
        while j>0 and arr[j-1] > arr[j]:
            arr[j-1] , arr[j] = arr[j] , arr[j-1]
            j -= 1

    return arr

if __name__ == "__main__":
    arr = [13 , 46 , 24 , 20 , 52 , 9]
    print(insertion_sorting(arr))