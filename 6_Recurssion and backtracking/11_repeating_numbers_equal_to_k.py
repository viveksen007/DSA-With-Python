# we are given an array , we are also given a target sum - a number can be repeated infinite times to get the targetted sum

def Repeating_sum (i , arr , temp , target):

    n = len(arr)

    if i >= n:
        if target == 0 :
            print(temp)
            return 
        else :
            return
    
    
    if arr[i] <= target:
        temp.append(arr[i])
        Repeating_sum(i , arr , temp , target - arr[i])
        temp.remove(arr[i])
    
    Repeating_sum(i + 1 , arr, temp , target)


if __name__ == "__main__":

    arr = [2 ,3 , 6 , 7]
    target = 7
    i = 0
    temp = []
    s = 0

    Repeating_sum(i , arr ,temp , target)