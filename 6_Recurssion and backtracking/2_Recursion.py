def Sum(n):

    if n == 0:
        return 0
    
    return (n + Sum(n-1))


if __name__ == "__main__":
    print(Sum(25))