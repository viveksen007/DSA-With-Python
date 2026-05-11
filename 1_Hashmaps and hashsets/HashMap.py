string = "aaaaaaabbbbbbbbbcccccccccccceeeeeeeee"

set = set(string)
freq  = {}

for S in string :
    freq[S] = freq.get(S , 0) + 1

print(freq)
