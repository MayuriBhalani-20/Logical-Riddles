'''
Create a function that takes a list and string. 
The function should remove the letters in the string from the list, and return the list.

===========
Test Cases
===========
remove_letters(["s", "t", "r", "i", "n", "g", "w"], "string") ➞ ["w"]

remove_letters(["b", "b", "l", "l", "g", "n", "o", "a", "w"], "balloon") ➞ ["b", "g", "w"]

remove_letters(["d", "b", "t", "e", "a", "i"], "edabit") ➞ []

'''
def remove_letters(list1,  string1):
    list2 = list1.copy()

    for i in list1:
        for j in string1:
            if i == j:
                list2.remove(i)
                string1 = string1[:string1.index(j)] + string1[string1.index(j) + 1:]
                i = ''
                break

    
    return list2

# m = remove_letters(["b", "b", "l", "l", "g", "n", "o", "a", "w"], "balloon") 
# m = remove_letters(["s", "t", "r", "i", "n", "g", "w"], "string") 
m = remove_letters(["d", "b", "t", "e", "a", "i"], "edabit") 
print(m)


