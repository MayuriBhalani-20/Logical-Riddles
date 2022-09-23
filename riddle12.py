'''Create a Python function that accepts a string. The function should return a string, with each character in the original string doubled. If you send the function "now" as a parameter, it should return "nnooww," and if you send "123a!", it should return "112233aa!!".
'''


def test(string1):
    str1 = ''
    for i in string1:
        str1 = str1 + '' + str(2*i)   
    
    return str1
        
m = test("now")
print(m)