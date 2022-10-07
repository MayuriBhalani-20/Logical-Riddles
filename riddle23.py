'''
Given an array, rotate the array to the right by k steps, where k is non-negative.

 

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
'''
# def test(list1):
#     i = 0
#     temp_list = list1.copy()
#     list2 = []
#     while i < len(temp_list): 
#         b = temp_list[i]
#         if b >= 10:
#             list2.append("True")
#             i = i+1
#         else:
#             list2.append("False")
#             i = i+1

# print(test([3,30,34,5,9]))            

def test(input_list, target):
    list1 = input_list
    ans_list = list1.copy()
    for i in range(target):
        ans_list = [ans_list[-1]] + ans_list[:-1]
        
    return ans_list
    
    

m = test([-1,-100,3,99], 2)
print(m)