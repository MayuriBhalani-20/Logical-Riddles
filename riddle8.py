'''
For this problem, we'll round an int value up to the next multiple of 10 if its rightmost digit is 5 or more, so 15 rounds up to 20. Alternately, round down to the previous multiple of 10 if its rightmost digit is less than 5, so 12 rounds down to 10. Given 3 ints, a b c, return the sum of their rounded values. To avoid code repetition, write a separate helper "def round10(num):" and call it 3 times. Write the helper entirely below and at the same indent level as round_sum().


round_sum(16, 17, 18) → 60
round_sum(12, 13, 14) → 30
round_sum(6, 4, 4) → 10
'''


def round_sum(n):
    m = str(n) 
    if len(m) == 1:
        if m < str(5):
            return "0"
        else:
            return "10"
    else:     
        if m[-1] < str(5):
            return m[ : -1] + "0"
        else:
            return m[ : -2] + str(int(m[-2])+1) + "0"     

def sum(a,b,c):
    a = round_sum(a)
    b = round_sum(b)
    c = round_sum(c)
    
    r = int(a) + int(b) + int(c)
    h = str(r)
    
    return "Ans : " + h

k = sum(6,4,4)
print(k)

# n = 234
# m = str(n) 
# k = m[len(m)-1] 
# print(k)