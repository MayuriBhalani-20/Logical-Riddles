'''
Given 3 int values, a b c, return their sum. However, if any of the values is a teen -- in the range 13..19 inclusive -- then that value counts as 0, except 15 and 16 do not count as a teens. Write a separate helper "def fix_teen(n):"that takes in an int value and returns that value fixed for the teen rule. In this way, you avoid repeating the teen code 3 times (i.e. "decomposition"). Define the helper below and at the same indent level as the main no_teen_sum().


no_teen_sum(1, 2, 3) → 6
no_teen_sum(2, 13, 1) → 3
no_teen_sum(2, 1, 14) → 3
'''

# def check_teen(n):
#     teen = [13, 14, 17, 18, 19]
    
#     if n in teen:
#         return 0
#     else:
#         return n

def test(a,b,c):
    
    # a = check_teen(a)
    # b = check_teen(b)
    # c = check_teen(c)
    teen = [13, 14, 17, 18, 19]
    list1 = []
    list1.append(a)
    list1.append(b)
    list1.append(c) 
    
    if a in teen:
        list1.remove(a)
    if b in teen:
        list1.remove(b)
    if c in teen:
        list1.remove(c)
        
    final_ans = sum(list1)
    
    return "Ans : " + str(final_ans)    #  str(a + b + c)

m = test(2,1,14)
print(m)