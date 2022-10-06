'''
we are given a matrix like [[1,2], [3,4]] and we have to count total negative number from the given matrix in a single loop
'''


def test(matrix1):
    i = 0
    j = 0
    count = 0 
    while i < len(matrix1):
        a = matrix1[i]
        if j < len(a):
            b = a[j]
            if b < 0:
                count = count + 1
                j = j + 1
            else:
                j = j+1
        else:
            i = i + 1
            j = 0
    return count
            
        
m = test([[-1,-2],[-3,-4]]) 
print(m)       