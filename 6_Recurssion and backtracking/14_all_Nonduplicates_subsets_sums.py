def SubSetSum ( i ,arr , temp , ans):

    n = len(arr)
    if i >= n:
        ans.add(tuple(sorted(temp)))
        return

    temp.append(arr[i])

    SubSetSum(i+1 , arr , temp , ans)

    temp.remove(arr[i])

    SubSetSum(i+1 , arr , temp , ans)

if __name__ == "__main__":
    arr = [1 , 2 , 2 ]
    i = 0
    ans = set()
    temp = []

    SubSetSum(i , arr , temp , ans)

    result = [list(Tup) for Tup in ans]
    print(result)
