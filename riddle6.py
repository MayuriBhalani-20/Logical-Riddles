'''
Given 3 int values, a b c, return their sum. However, if one of the values is 13 then it does not count towards the sum and values to its right do not count. So for example, if b is 13, then both b and c do not count.


lucky_sum(1, 2, 3) → 6
lucky_sum(1, 2, 13) → 3
lucky_sum(1, 13, 3) → 1
'''

def lucky_sum(a,b,c):
    list1 = []
    list1.append(a)
    list1.append(b)
    list1.append(c) 
    if a == 13:
        list1.remove(a)
        list1.remove(b)
        list1.remove(c)
    elif b == 13:
        list1.remove(b)
        list1.remove(c)
    elif c == 13:
        list1.remove(c)
        
    final_ans = sum(list1)
    
    return "Ans : " + str(final_ans)

m = lucky_sum(13,13,3)
print(m)