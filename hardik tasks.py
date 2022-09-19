# class Solution:
#    def solve(self, nums):
#       return sorted(x * x for x in nums)
# ob = Solution()
# nums = [-2, 0, 4, -8, 6]
# print(ob.solve(nums))


# li = [-2, 0, 4, -8, 6]
# m = len(li)
# print(m) 
    
# b=sorted(list(map(lambda x:x*x, li)))
# print(b)


def sortArrays(arr):
    length = len(arr)
    j = 0
    while j < length - 1: 
        if (arr[j]** 2 > arr[j + 1]** 2): 
            temp = arr[j] ** 2
            arr[j] = arr[j + 1] ** 2
            arr[j + 1] = temp
            j = -1   
        j += 1       
    return arr

list1 = [-2, 0, 4, -8, 6, -8]
print(sortArrays(list1))
