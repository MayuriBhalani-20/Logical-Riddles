'''
We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) and big bricks (5 inches each). Return True if it is possible to make the goal by choosing from the given bricks. This is a little harder than it looks and can be done without any loops. See also: Introduction to MakeBricks


make_bricks(3, 1, 8) → True
make_bricks(3, 1, 9) → False
make_bricks(3, 2, 10) → True
'''



def make_briks(small, big, goal):
    l1 = [i for i in range(1,small+1)]
    l2 = [i*5 for i in range(1,big+1)]
    i = 0
    j = 0
    l3 = []
    while len(l1) > i:
        m = l1[i] + l2[j]
        l3.append(m)
        if len(l2)-1 > j:
            j = j+1
        else:
            j = 0
            if len(l1)-1 > i:
                i = i+1
            else:
                i = i+1
    
    if goal in l1:
        a = True
    elif goal in l2:
        a = True
    elif goal in l3:
        a = True
    else:
        a = False            
              
    return a
        
a = make_briks(2, 10, 16)
print(a)

# l1 = [1,2]
# l2 = [5,10]
# l1 = [i for i in range(1,n-1)]

# def test():
#     l1 = [1,2]
#     l2 = [5,10]
#     i = 0
#     j = 0
#     l3 = []
#     while len(l1) > i:
#         a = l1[i] + l2[j]
#         l3.append(a)
#         if len(l2)-1 > j:
#             j = j+1
#         else:
#             j = 0
#             if len(l1)-1 > i:
#                 i = i+1
#             else:
#                 i = i+1  
    
                
#     return l3
    
# m = test()
# print(m)