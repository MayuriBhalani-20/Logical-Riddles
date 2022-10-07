'''
Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.

 

Example 1:

Input: nums = [10,2]
Output: "210"
Example 2:

Input: nums = [3,30,34,5,9]
Output: "9534330"
'''


def test(input_list):
    empty_list = []
    ans_list = []
    ans_string = ""
    for i in input_list:  
        a = str(i)
        ans_list.append(a)
    
    i = 0
    temp_list = ans_list.copy()
    while i < len(temp_list):
        if ans_list == empty_list:
            break 
        b = max(ans_list)
        if int(b) >= 10: 
            if b[0] in ans_list and b[1] < b[0]:
                for n in ans_list:
                    if b[0] == n:
                        ans_string = ans_string + n
                        ans_list.remove(n)
              
        ans_string = ans_string + b
        ans_list.remove(b)
        i = i + 1
        
    return ans_string
    
        
        
m = test([10,2])
print(m)
