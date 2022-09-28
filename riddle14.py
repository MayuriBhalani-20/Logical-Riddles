'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
'''
 
#TEST CASES:            
# a = test([2,7,9,3,1])  # Ans : 12
# a = test([6,7,1,3,8,2,4]) # Ans : 18
# a = test([5, 3, 4, 11, 2]) #Ans : 16



# def demo(list1):
#     list2 = []
#     list3 = []
#     i = 0
#     while len(list1) > i:
#             try:
#                 if i == 0:
#                     list2.append(list1[i])
#                     m = list1[i+2:]
#                     b = max(m)
#                     list2.append(b)
#                     i = list1.index(b, i+2, len(list1)-1)
#                 else:
#                     m = list1[i+2:]
#                     b = max(m)
#                     list2.append(b)
#                     i = list1.index(b, i+2, len(list1)-1)
#             except:
#                 i = i + 1
                
#     i = 1
#     while len(list1) > i:
#             try:
#                 if i == 1:
#                     list3.append(list1[i])
#                     m = list1[i+2:]
#                     b = max(m)
#                     list3.append(b)
#                     i = list1.index(b, i+2, len(list1)-1)
#                 else:
#                     m = list1[i+2:]
#                     b = max(m)
#                     list3.append(b)
#                     i = list1.index(b, i+2, len(list1)-1)
#             except:
#                 i = i + 1
    
#     m = sum(list2)
#     n = sum(list3)
#     if m >= n:
#         return m
#     else:
#         return n    

                
# a = demo([5, 3, 4, 11, 2])
# print(a)


def houseRobbery(input_list, temp_flag):
    answer_list = []
    if temp_flag:
        i = 0
    else:
        i = 1
    while len(input_list) > i:
        try:
            if i == 0:
                answer_list.append(input_list[i])
                sliced_list = input_list[i+2:]
                max_number = max(sliced_list)
                answer_list.append(max_number)
                i = input_list.index(max_number, i+2, len(input_list)-1)
            
            if i == 1:
                answer_list.append(input_list[i])
                sliced_list = input_list[i+2:]
                max_number = max(sliced_list)
                answer_list.append(max_number)
                i = input_list.index(max_number, i+2, len(input_list)-1)
            
            else:
                sliced_list = input_list[i+2:]
                max_number = max(sliced_list)
                answer_list.append(max_number)
                i = input_list.index(max_number, i+2, len(input_list)-1)
        except:
            i = i + 1
    return answer_list

def final_function(input_list):
    a = houseRobbery(input_list, True)
    b = houseRobbery(input_list, False)
    
    return max(sum(a), sum(b))

print(final_function([2,7,9,3,1]))