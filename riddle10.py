'''
Capital indexes
Write a function named capital_indexes. The function takes a single parameter, which is a string. Your function should return a list of all the indexes in the string that have capital letters.

For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4].
'''

def capital_index(string1):
    list1 = []
    for i in string1:
        if i.isupper():
            a = string1.index(i)
            list1.append(a) 
    return list1

m = capital_index("hardiK")
print(m)