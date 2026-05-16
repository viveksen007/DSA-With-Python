def Find_sum_targets(i , temp , arr , target  , S ):
    n = len(arr)
    if i >= n:
        if S == target:
            return 1
        else:
            return 0
    temp.append(arr[i])
    S += arr[i]
    L = Find_sum_targets(i+1 , temp , arr , target  , S )
    temp.remove(arr[i])
    S -= arr[i]
    R = Find_sum_targets(i+1 , temp , arr , target , S ) 

    return L + R


if __name__ == "__main__":
    arr = [ 5 , 2 , 0 ,3 ,1 , 2]
    i = 0 
    S = 0
    target = 5
    temp = []
    print(Find_sum_targets(i , temp , arr , target , S))