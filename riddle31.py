'''
Given a non-negative integer num, return true if num can be expressed as the sum of any non-negative integer and its reverse, or false otherwise.

 

Example 1:

Input: num = 443
Output: true
Explanation: 172 + 271 = 443 so we return true.


Example 2:

Input: num = 63
Output: false
Explanation: 63 cannot be expressed as the sum of a non-negative integer and its reverse so we return false.


Example 3:

Input: num = 181
Output: true
Explanation: 140 + 041 = 181 so we return true. Note that when a number is reversed, there may be leading zeros.
'''

# def test(num):
#     string1 = str(num)
#     last_num = string1[-1]
#     print(last_num)
    
# def first_last_combination(last_num):
#     if last_num == 0:
#         a = [(1,9), (2,8), (3,7), (4,6), (5,5)]
#     if last_num == 1:
#         a = [(0,1) ]    
    

# def test(num):
#     if num%11==0:
#         print('Yes')
#     else:
#         if num%2==0 and num<20:
#             print('Yes')
#         else:
#             for j in range(11,(int(num)//2)+1):
#                 if j+int(str(j)[::-1])==num:
#                     print('Yes')
#                     break

def test(num):
    if num%11==0:
        return 'True'
    else:
        ans = num 
        n = str(ans)
        r = n[::-1]
        m = int(n)
        v = int(r)
        for i in range(11,ans):
            if m + v == num:
                return 'True' 
            else:
                m = m-1
                n = str(m)
                r = n[::-1]
                v = int(r)
        return 'False'                  
                
m = test(146674)
print(m)

'''
NOTE = palidrone numbers will always return true for this question and every multiple of 11 will also return true. 
'''

# def combination(num):
#     string1 = str(num)
#     last_number = string1[-1]
#     list1 = []
    
#     for i in range(int(last_number)):
#         n = int(last_number) - i
#         list1.append((i,n))
#     # a = set(list1)
#     final_list = list(set(list1))                
#     print(final_list)  

# m = combination(443)
# print(m)



# m = '443'
# s = m[::-1]
# print(m)
# print(s)