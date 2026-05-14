def Reverse(arr , i  , temp):

    if i < 0 :
        return 
    
    temp.append(arr[i])
    Reverse(arr , i-1 , temp)



if __name__ == "__main__":
    arr = [ 1 ,2 ,4 ,3 , 2]
    n = len(arr)
    temp = []   
    Reverse(arr , n-1 , temp)
    print(temp)

    