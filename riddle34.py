'''
Input : n = 2, m = 3
Output : 2 4 6 

Input : n = 3, m = 4
Output : 3 6 9 12 

- using for loop  
- starting point from 'n'
- ending point to 'm'
- in between the output is 
        3*1
        3*2
        3*3
        3*4


'''

n = 2
m = 3

result_list = []
for i in range(1,m+1):
    k = i*n
    result_list.append(k)

print(result_list)


