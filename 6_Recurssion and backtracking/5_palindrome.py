def Is_palindrome(s , i):
    n = len(s)

    if i >= int(n/2) :
        return True 
    
    if s[i] != s[n-1-i]:
        return False
    
    return Is_palindrome(s , i+1)


if __name__ == "__main__":
    s = "madsm"
    i = 0
    print(Is_palindrome(s , i))