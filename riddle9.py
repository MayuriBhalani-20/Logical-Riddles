'''
We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each). Return the number of small bars to use, assuming we always use big bars before small bars. Return -1 if it can't be done.


make_chocolate(4, 1, 9) → 4
make_chocolate(4, 1, 10) → -1
make_chocolate(4, 1, 7) → 2
'''


def make_chocolate(small, big, goal):
    big1 = big*5 
    if goal == big1:
        return 0
    else:
        a = goal - big1
        if a <= small:
            return a
        else:
            return -1
        
        
m = make_chocolate(4,1,7)
print(m)