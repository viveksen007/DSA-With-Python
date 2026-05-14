def Reverse (a , l , r ):
    
    if l >= r:
        return 
    
    a[l] , a[r] = a[r] , a[l]

    Reverse(arr , l+1 , r-1 )


if __name__ == "__main__":
    arr = [1 ,2 , 3 ,4 , 2]
    l = 0
    r = len(arr)
    Reverse(arr , l , r-1 )
    print(arr)




