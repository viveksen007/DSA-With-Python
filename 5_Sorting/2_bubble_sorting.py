# bubble sort

def bubble_sorting(arr):

    n = len(arr)
    didSwap = 0

    for i in range(n-1 , 0 , -1):
        for j in range(0 , i):
            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1] , arr[j]
                didSwap = 1

        if didSwap == 0:
            break
    print("runs!")
    return arr

if __name__ == "__main__":          
    arr = [13 , 46 , 24 , 20 , 52 , 9]
    print(bubble_sorting(arr))