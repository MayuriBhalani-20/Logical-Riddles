'''
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.
'''


def ySection(y1, y):
    return (y - y1)

def xSection(m, x1, x):
    return (m * (x - x1))

def checkStraightLine(coordinates):
    a = coordinates[0]
    b = coordinates[1]
    m = (a[1] - b[1])/(a[0] - b[0])
    count = 0
    for i in coordinates:
        x = i[0]
        y = i[1]
        
        # x_ans = x_section(m, a[0], x) 
        # y_ans = y_section(a[1], y)
        x_ans = (m * (x - a[0])) 
        y_ans = (y - a[1])
        
        if x_ans == y_ans:
            count += 1 
    # y - a[1] = m(x - a[0])
    if count == len(coordinates):
        return True
    else:
        return False
        
# m = test([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]])
m = checkStraightLine([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]])
print(m)