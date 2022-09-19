li = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

for i in li:
    print(i, end=" ")
    
for i in range(65,70):
    k=i
    # Inner loop
    for j in range(65,i+1):
        print(chr(k),end="")
        k=k+1
    print()
    
    
for i in li:
    k=i
    l = int(i+1)
    # Inner loop
    for j in range(l): 
        print(chr(k),end="")
        k=k+1
    print()
    
