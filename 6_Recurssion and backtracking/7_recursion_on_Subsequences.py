def Subsequences(i , temp , arr):
    n = len(arr)

    if i >= n:
        print(temp)
        return 
    temp.append(arr[i])
    Subsequences(i+1 , temp , arr)
    temp.remove(arr[i])
    Subsequences(i+1 , temp , arr)


if __name__ == "__main__":
    arr = [3 , 1 , 2]
    i = 0
    temp = []
    Subsequences(i , temp , arr)