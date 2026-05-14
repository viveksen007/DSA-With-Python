def Reverse(arr , i ):
    n = len(arr)
    if i >= int(n/2):
        return
    
    arr[i] , arr[n-i-1] = arr[n-1-i] , arr[i]
    Reverse(arr , i+1)

if __name__ == "__main__":
    arr = [1 ,2 , 3 ,4 , 2]
    l = 0
    Reverse(arr , l )
    print(arr)
