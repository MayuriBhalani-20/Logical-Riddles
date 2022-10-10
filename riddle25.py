'''
Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.

You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.

 

Example 1:

Input: nums = [1,2,1,3,2,5]
Output: [3,5]
Explanation:  [5, 3] is also a valid answer.
Example 2:

Input: nums = [-1,0]
Output: [-1,0]
Example 3:

Input: nums = [0,1]
Output: [1,0]
'''

def test(a):
    i = 0
    ans = []

    while i < len(a):
        if len(a) == 1:
            ans.append(a[i])
            break
        temp = a[i]
        a.pop(i)
        if temp not in a:
            ans.append(temp)
            a = [temp] + a
            i = i+1
            continue
        a = [temp] + a
        i = i+1
        
    return ans

m = test([1,2,1,3,2,5])
print(m)