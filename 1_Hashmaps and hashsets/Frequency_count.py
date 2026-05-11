def frequency_count (arr):
    freq = {}

    for nums in arr :
        freq[nums] = freq.get(nums , 0) + 1

    return freq

if __name__ == "__main__" :
    A = [ 2, 5 , 7 , 8 , 8 , 9 , 2 , 5 , 2 , 7 , 7 , 7]

    B = frequency_count(A)
    print(B)