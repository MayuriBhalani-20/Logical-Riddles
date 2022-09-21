'''
NOTE: the question is same as riddle 3, this is the alternate way of riddle 3
'''

def KMPSearch(pat, txt):
    m = len(pat)
    n = len(txt)
    count = 0
    
    for i in range(n):
        a = txt[i:i+m]
        if a == pat:
            count = count +1
            
            
    return "Ans : " + str(count)


txt = "geeksforgeeksforgeeks"
pat = "geeksforgeeks"
a = KMPSearch(pat, txt)
print(a)