'''
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
'''


# def test(list1, target):
#     count = 0 
            
#     for i in list1:
#         if i == target:
#             return count
#         count = count+1
        
#     return -1


def binarySearch(list1, target):
    left = 1
    right = len(list1)-1
    
    if target in list1:
        while left <= right:

            mid = (left+right) //2

            if list1[mid] == target:
                return mid
            elif list1[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
    else:
        return -1
    
    

a = [-1,0,3,5,9,12]
m = binarySearch(a, 2)
print(m)