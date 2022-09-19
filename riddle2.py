# Question : we have given a string and we need to find a word that occurs maximum time in the string with its count of occurance.


import string

def word_count(string1):
    # punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    counts = dict()
    # for i in str:
    #     if i == punc:
    #         test_str = test_str.replace(i, "")
    new_str = string1.translate(str.maketrans('', '', string.punctuation))               
    words_list = new_str.split()
    
    for word in words_list:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    
    ans = max(counts, key=counts.get)
    return str(ans) + " :- " + str(counts[ans])

a = word_count('Hello My name is Mayuri, Mayuri is a python developer Mayuri joined compnay 1 and half month ago.') 
print(a)    
        
        
    
    
    
    
# def countOccurrences(str, word):
#     # split the string by spaces in a
#     a = str.split(" ")
#     # search for pattern in a
#     count = 1
#     print(len(a))
#     for i in range(0, len(a)):      
#         # if match found increase count
#         if (word == a[i]):
#            count = count + 1
#     return count       

# str ="Hello My name is Mayuri, Mayuri is a python developer. Mayuri joined compnay 1 and half month ago."
# word ="Mayuri"
# print(countOccurrences(str, word))    