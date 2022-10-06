'''
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []
'''


# def double_number(input_list, target):
#     ans_set = set()
#     ans_list = []
#     for i in input_list:
#         m = i
#         temp_set = {i}
#         while m < target:
#             a = target - m
#             if a in input_list:
#                 temp_set.add(a)
#                 ans_set.add(frozenset(temp_set))
#                 m = sum(temp_set)
#             else:
#                 temp_set.add(a)
#                 m = sum(temp_set)
#     for x in ans_set:
#         b = list(x)
#         ans_list.append(b)            
#     return ans_list

# b = double_number([2,3,4,5,6,7], 7)     
# print(b)



# def demo(input_list, target):
#     ans_list = []
#     for i in input_list:
#         if i == target:
#             ans_list.append([i])
#         else:
#             m = i 
#             temp_list = []
#             while m < target:
#                 temp_list.append(i)             #####
#                 m = sum(temp_list)
#                 if m == target:
#                     ans_list.append(temp_list)
#                 a = target - m 
#                 if a > i:
#                     temp_list.append(i)
#                     m = sum(temp_list)
#                 elif a < 0 :
#                     temp_list.pop(len(temp_list)-1)
#                     m = sum(temp_list)
#                     a = target - m
#                     if a < i :
#                         temp_list.pop(len(temp_list)-1)
#                     for n in input_list:
#                         temp_list.append(n)
#                         m = sum(temp_list)
#                         if m == target:
#                             ans_list.append(temp_list)
#                             break
#                         a = target - m 
#                         if a >= n:
#                             for r in range(len(input_list)):
#                                 temp_list.append(n)
#                                 m = sum(temp_list)
#                                 if m == target:
#                                     ans_list.append(temp_list)
#                                     break
#                                 elif m > target:
#                                     temp_list.pop(len(temp_list)-1)
#                                     r = range(len(input_list) + 1) 
#                         temp_list.pop(len(temp_list)-1)
    
#     return ans_list

# b = demo([2,3,4,5,6,7], 7)     
# print(b)


# def single_number(input_list, target):
#     ans_list = []
#     for i in input_list:
#         m = i 
#         temp_list = []
#         while m < target:
#             temp_list.append(i)             
#             m = sum(temp_list)
#             if m == target:
#                 ans_list.append(temp_list)
                
#     return ans_list

# b = single_number([2,3,4,5,6,7], 8)    ### ans --> [[2,2,2,2], [4,4]]
# print(b)

def test(input_list, target):
    ans_list1 = []
    ans_list = []
    for i in input_list:
        m = i 
        temp_list = [i]
        while m < target:
            temp_list.append(i)             
            m = sum(temp_list)
        ans_list1.append(temp_list)
        
    for i in ans_list1:
        mayuri = i.copy()
        for j in i:
            
            mayuri.pop()
            
            sum1 = sum(mayuri)
            b = target - sum1
            if b in input_list:
                mayuri.append(b)
                ans_list.append(mayuri)
                right_pointer = (len(mayuri) - 1)
                while right_pointer > 0:
                    tinu =[]
                    tinu = mayuri.copy()
                    mom = mayuri[right_pointer] + mayuri[(right_pointer)-1]
                    if mom in input_list:
                        tinu.pop(right_pointer)                
                        tinu.pop((right_pointer)-1)
                        tinu.append(mom)
                        ans_list.append(tinu)
                        
                    right_pointer = right_pointer - 1                
                
                                    
    ans_list1 = []
    for i in ans_list:
        a = sorted(i)
        ans_list1.append(a)
        
    final_list = []
    for i in ans_list1:
        if i not in final_list:
            final_list.append(i)
        
    return final_list            

b = test([2,3,4,5,6,7], 9)
print(b)    


# def final_ans(list1):
    
#     list1 = list(list1)
#     ans_list = []
    
#     for i in list1:
#         a = sorted(i)
#         ans_list.append(a)
        
#     final_list = []
#     for i in ans_list:
#         if i not in final_list:
#             final_list.append(i)
        
#     return final_list
    
   
       

# m = final_ans([[2, 2, 3], [2, 2, 3], [3, 4], [4, 3], [4, 3], [5, 2], [5, 2], [7]])
# print(m)

# def test(input_list, target):
#     ans_list = []
#     for i in input_list:
#         if i == target:
#             ans_list.append([i])
#         else:
#             m = i
#             temp_list = [i]
#             list3 =[i]
            # while m < target:
            #     temp_list.append(i)
            #     m = sum(temp_list)
            #     if m == target:
            #         ans_list.append(temp_list)
            #     elif m < target:
            #         for i in input_list:
            #             temp_list.append(i)
            #             m = sum(temp_list)
            #             if m == target:
            #                 ans_list.append(temp_list)
            #             temp_list.pop(len(temp_list) - 1)
            #         temp_list.append(i)
#     return ans_list
                    

# b = test([2,3,4,5,6,7], 7)
# print(b)


# a = [1,2,3,4,5]
# b = a
# b[0] = 10
# print(a)
# print(b)

# c = a.copy()
# c[0] = "abc"
# print(c)
# print(a)