def Max_sum(arr, k):
    seen = {}
    for i, num in enumerate(arr):
        complement = k - num
        if complement in seen:
            return f"The indices are: ({seen[complement]}, {i})"
        seen[num] = i
    return "No such subarray found."

if __name__ == "__main__":
    Array = [4 , 9 ,5 , 3 ,0 ,4]
    k = 8
    print(Max_sum(Array , k))