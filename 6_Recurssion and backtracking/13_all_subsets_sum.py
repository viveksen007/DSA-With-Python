def SubsetSum (i , arr , temp , ans):

    n = len(arr)

    if i >= n:
        Sum = sum(temp)
        ans.append(Sum)
        ans.sort()
        return 
    

    temp.append(arr[i])

    SubsetSum(i+1 , arr , temp , ans)

    temp.remove(arr[i])

    SubsetSum(i+1 , arr , temp ,ans)


if __name__ == "__main__":

    arr = [ 5 , 2 , 1]
    i = 0 
    temp = []
    ans = []

    SubsetSum(i , arr , temp , ans)

    print(ans)