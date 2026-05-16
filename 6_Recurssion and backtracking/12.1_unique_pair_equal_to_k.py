# given an array and a target , give the pairs of array which is equal to sum but all should be unique 

# we are given an array , we are also given a target sum - a number can be repeated infinite times to get the targetted sum

def Unique_Sum (i , arr , temp , target , ans):

    n = len(arr)

    if i >= n:
        if target == 0 :
            ans.add(tuple(temp))
            return 
        else :
            return
    
    
    if arr[i] <= target:
        temp.append(arr[i])
        Unique_Sum(i + 1 , arr , temp , target - arr[i] , ans)
        temp.remove(arr[i])
    
    Unique_Sum(i + 1 , arr, temp , target , ans)


if __name__ == "__main__":

    arr = [1 , 2 , 1 , 2 , 2]
    arr.sort()
    print(arr)
    target = 4
    i = 0
    temp = []
    ans = set()

    Unique_Sum(i , arr ,temp , target , ans)

    result = [list(tup) for tup in ans]
    print(result)
