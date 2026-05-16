def Unique_sum (ind , arr ,temp , target , ans):

    n = len(arr)

    if target == 0 :
        ans.add(tuple(sorted(temp)))
        return 

    for i in range(ind , n):

        if(i > ind and arr[i] == arr[i-1]):
            continue

        if arr[i] > target :
            break

        temp.append(arr[i])
        Unique_sum(i + 1 , arr , temp , target - arr[i] , ans)
        temp.remove(arr[i]) 

if __name__ == "__main__":
    arr = [1 ,1 , 1 , 2 , 2]
    target = 4 
    arr.sort()
    ind = 0
    temp =  []
    ans = set()

    Unique_sum(ind , arr ,temp , target , ans)

    result = [list(tup) for tup in ans]
    print(result)
