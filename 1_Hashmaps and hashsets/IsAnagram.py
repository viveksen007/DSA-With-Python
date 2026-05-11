def Is_Anagram(S1 , S2):

    S1 = S1.Lower()
    S2 = S2.lower()

    if len(sorted(S1)) != len(sorted(S2)):
        return False

    freq = {}

    for ch in S1 :
        freq[ch] = freq.get(ch , 0) + 1

    for ch1 in S2 :
        if ch1 in freq or freq[ch1] == 0:
            return False
        freq[ch1] -= 1

        
if "__name__" == "__main__":

    S1 = "silent"
    S2 = "listen"
    B = Is_Anagram(S1 , S2)
    print(B)