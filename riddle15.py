'''
Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

A shift on s consists of moving the leftmost character of s to the rightmost position.

For example, if s = "abcde", then it will be "bcdea" after one shift.
 

Example 1:

Input: s = "abcde", goal = "cdeab"
Output: true

Example 2:

Input: s = "abcde", goal = "abced"
Output: false
'''


def test(input_string, goal):
    list1 = [input_string]
    for i in range(len(input_string) - 1 ):
        i = 0
        temp = input_string[i]
        
        a = input_string.replace(temp, "")
        
        string1 = a + temp
        
        list1.append(string1)

        input_string = string1
        
    if goal in list1:
        return True
    else:
        return False
    

m = test("abcde", "cdeab")
print(m)


# def test(s, goal):
#     answer = ""    
#     answer_list = []
        
#     for i in range(len(s)):    
#         a = s[:i+1] 
        
#         answer = s.replace(a, "") + a
#         answer_list.append(answer)
        
#     if goal in answer_list:
#         return True
#     else:
#         return False