'''
Given an integer array nums, return the number of subarrays filled with 0.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,3,0,0,2,0,0,4]
Output: 6
Explanation: 
There are 4 occurrences of [0] as a subarray.
There are 2 occurrences of [0,0] as a subarray.
There is no occurrence of a subarray with a size more than 2 filled with 0. Therefore, we return 6.

Example 2:

Input: nums = [0,0,0,2,0,0]
Output: 9
Explanation:
There are 5 occurrences of [0] as a subarray.
There are 3 occurrences of [0,0] as a subarray.
There is 1 occurrence of [0,0,0] as a subarray.
There is no occurrence of a subarray with a size more than 3 filled with 0. Therefore, we return 9.

Example 3:

Input: nums = [2,10,2019]
Output: 0
Explanation: There is no subarray filled with 0. Therefore, we return 0.
'''

 
def test(list1):
    final_list = []
    i = 0
    j = 1
    while i < len(list1):
        if list1[i] != 0:
            i = i+1
            j = j+1
        else:
            while j < len(list1):
                if list1[j] == 0:
                    m = list1[i:j+1]
                    j = j+1
                else:
                    break
            final_list.append(m)
            i = j 
            j = i+1
    ans = 0
    for i in final_list:
        k = combination_ans(i)
        ans = ans + k
    
    return ans
        
        
def combination_ans(list1):
    
    m = range(len(list1)+1)
    sum1 = sum(m)
    
    return sum1
            
            
        
    
    
k = test([0,0,0,1])
print(k)


    
