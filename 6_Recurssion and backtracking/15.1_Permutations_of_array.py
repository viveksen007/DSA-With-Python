def Permutations ( arr , temp , freq):

    n = len(arr) 

    if len(temp) == n:
        print(temp)
        return
    
    for i in range(0 , n):

        if freq[arr[i]] > 0 :
            temp.append(arr[i])
            freq[arr[i]] -= 1
            Permutations(arr , temp , freq)
            temp.remove(arr[i])
            freq[arr[i]] += 1

if __name__ == "__main__":

    freq = {}


    arr = [1 , 2 , 3]
    i = 0
    temp = []
    ans = []

    for nums in arr :
        freq[nums] = freq.get(nums , 0) + 1

    Permutations(arr, temp , freq)

    
