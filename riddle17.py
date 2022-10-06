'''
Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.

If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.

 

Example 1:

Input: s = "abcdefg", k = 2
Output: "bacdfeg"
Example 2:

Input: s = "abcd", k = 2
Output: "bacd"

'''

def index_reverse(input_string, k):
    if k <= len(input_string):
        m = len(input_string)
        b = m//2
        for i in range(b):
            if i == 0:
                prev = 0    
            temp = (i+1) * k
            a = input_string[prev:temp]
            if i%2 == 0:
                new_string = a[::-1]
                input_string = input_string.replace(a, new_string)
            prev = temp
    else:
        input_string = input_string[::-1]
    return input_string


m = index_reverse("abcd",2)
print(m)


## THIS FUNCTION IS USED FOR PERFORMING OPERATION WHERE WE JUST WANT TO REVERSE K NUMBERS FROM THE STARTING OF THE STRING

# def index_reverse(input_string, k):
#     if k <= len(input_string):
#         new_string = input_string[:k]
#         a = new_string[::-1]
#         final_string = input_string.replace(new_string, a)
#     else:
#         final_string = input_string[::-1]
#     return final_string