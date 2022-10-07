'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
'''

def demo(num1, num2):
    num3 = num1 + num2
    print(num3)
    a = len(num3)//2 
    
    if len(num3) % 2 == 0:
        b = num3[a] + num3[a-1]
        return b/2
    else:
        return num3[a]
    
m = demo([1,2], [3,4])
print(m)

# def findMedianSortedArrays(nums1, nums2):
#     if not nums1 or not nums2:
#         nums = nums1 if nums1 else nums2
#         length = len(nums)
#         if length % 2 == 0:
#             return (nums[length // 2] + nums[length // 2 - 1]) / 2
#         else:
#             return nums[length // 2]
 
#     target = (len(nums1) + len(nums2)) // 2
 
#     def helper(low, high, A, B):
#         if low > high:
#             return None
#         else:
#             x = low + (high - low) // 2
#             y = target - x
#             if y == len(B):
#                 if B[y - 1] > A[x]:
#                     return helper(x + 1, high, A, B)
#             elif y == 0:
#                 if B[y] < A[x]:
#                     return helper(low, x - 1, A, B)
#             else:
#                 if B[y - 1] > A[x]:
#                     return helper(x + 1, high, A, B)
#                 if B[y] < A[x]:
#                     return helper(low, x - 1, A, B)    
#             if (len(A) + len(B)) % 2 == 1:
#                 return A[x]
#             else:
#                 the_other = float('-inf')
#                 if x - 1 >= 0:
#                     the_other = max(A[x - 1], the_other)
#                 if y - 1 >= 0:
#                     the_other = max(B[y - 1], the_other)
#                 return (A[x] + the_other) / 2    
 
#     res = helper(max(0, target - len(nums2)), min(len(nums1) - 1, target), nums1, nums2)
#     if res:
#         return res
#     return helper(max(0, target - len(nums1)), min(len(nums2) - 1, target), nums2, nums1)
 
# print(findMedianSortedArrays([1,2],[3,4]))