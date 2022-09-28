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
        # index = b         
    return "Middle element is: " + m

ans = mid("mayuris")
# ans = mid("abcmaaahjet")

print(ans)
    
    
'''
Same question as above, in addition, we have to also get the index of the middle element!!
(it is possible just add commented line in the code)
'''    