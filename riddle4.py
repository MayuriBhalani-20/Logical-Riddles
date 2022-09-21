'''
Question:
Given 3 int values, a b c, return their sum. However, if one of the values is the same as another of the values, it does not count towards the sum.


lone_sum(1, 2, 3) → 6
lone_sum(3, 2, 3) → 2
lone_sum(3, 3, 3) → 0
'''


def lone_sum(a,b,c):
    list1 = []
    list1.append(a)
    list1.append(b)
    list1.append(c)        
    if a == b and b == c:
        list1.remove(a)
        list1.remove(b)
        list1.remove(c)
    elif a == b:
        list1.remove(a)
        list1.remove(b)
    elif a == c:
        list1.remove(a)
        list1.remove(c)
    elif b == c:
        list1.remove(b)
        list1.remove(c)
    
    final_ans = sum(list1)
    
    return "ans : " + str(final_ans)
    
        
a = lone_sum(3,3,3)
print(a)