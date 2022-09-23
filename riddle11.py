'''
Middle letter
Write a function named mid that takes a string as its parameter. Your function should extract and return the middle letter. If there is no middle letter, your function should return the empty string.

For example, mid("abc") should return "b" and mid("aaaa") should return "".
'''


def mid(string1):
    a = len(string1)
    b = a//2
    c = a%2
    # print(c)
    # print(type(c))
    # if type(c) == float:   
    if c == 0:   
        m = "''"     
    else:
        m = string1[b]     
    return m

ans = mid("mayuris")
print(ans)
    
    
h = "abcmahjet"