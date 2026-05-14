def First_Equals_to_Sum(i , temp , arr , target  , S):
    n = len(arr)
    if i >= n:
        if S == target:
            print(temp)
            return True 
        else :
            return False 
    temp.append(arr[i])
    S += arr[i]
    if First_Equals_to_Sum(i+1 , temp , arr , target  , S) == True :
        return True 
    temp.remove(arr[i])
    S -= arr[i]
    if First_Equals_to_Sum(i+1 , temp , arr , target , S) == True:
        return True

    return False 


if __name__ == "__main__":
    arr = [ 5 , 2 , 0 ,3 ,1 , 2]
    i = 0 
    S = 0
    target = 5
    temp = []
    First_Equals_to_Sum(i , temp , arr , target , S)