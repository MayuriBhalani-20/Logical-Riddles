grid = [[0,0,0,0,0,0,0,0]]

# grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
#         [0,0,0,0,0,0,0,1,1,1,0,0,0],
#         [0,1,1,0,1,0,0,0,0,0,0,0,0],
#         [0,1,0,0,1,1,0,0,1,0,1,0,0],
#         [0,1,0,0,1,1,0,0,1,1,1,0,0],
#         [0,0,0,0,0,0,0,0,0,0,1,0,0],
#         [0,0,0,0,0,0,0,1,1,1,0,0,0],
#         [0,0,0,0,0,0,0,1,1,0,0,0,0]]


def test(matrix1):
    m = len(matrix1)
    list1 = [0]
    for i in range(m):
        n = len(matrix1[i])
        for j in range(n):
            current = matrix1[i][j]
            if current == 1:
                ans = reccur_fun(matrix1, i ,j)
                list1.append(ans)
    # print(list1)
    return max(list1)


def reccur_fun(matrix1, i, j):
    # current = matrix1[i][j]
    matrix1[i][j] = 0
    count = 1
    
    try:
        
        if matrix1[i+1][j] == 1:
            # count = count + 1
            matrix1[i+1][j] = 0
            
            a = reccur_fun(matrix1, i+1, j)
            count += a
    except:
        pass
    try:
        if matrix1[i][j+1] == 1:
            # count = count + 1
            matrix1[i][j+1] = 0
            b = reccur_fun(matrix1, i, j+1)
            count += b
    except:
        pass
    try:
        if (j - 1) >= 0:
            if matrix1[i][j-1] == 1:
                # count = count + 1
                matrix1[i][j-1] = 0 
                c = reccur_fun(matrix1, i, j-1)
                count += c
        else:
            pass
    except:
        pass
    
    try:
        if (i-1) >= 0:
                    
            if matrix1[i-1][j] == 1:
                # count = count + 1
                matrix1[i-1][j] = 0 
                d = reccur_fun(matrix1, i-1, j)
                count += d
        else:
            pass
    except:
        pass
    
    return count  
                    

print(test(grid))
# print(reccur_fun(grid, 6, 7))
# print(grid[7][7])