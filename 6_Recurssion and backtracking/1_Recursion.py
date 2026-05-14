def Recursion(i , sum):

    if i < 1:
        print(sum)
        return 
    
    Recursion(i-1 , sum + i)

if __name__ == "__main__":
    Recursion(25 , 0)