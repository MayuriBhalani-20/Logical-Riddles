'''
A sentence is a string of single-space separated words where each word can contain digits, lowercase letters, and the dollar sign '$'. A word represents a price if it is a sequence of digits preceded by a dollar sign.

For example, "$100", "$23", and "$6" represent prices while "100", "$", and "$1e5" do not.
You are given a string sentence representing a sentence and an integer discount. For each word representing a price, apply a discount of discount% on the price and update the word in the sentence. All updated prices should be represented with exactly two decimal places.

Return a string representing the modified sentence.

Note that all prices will contain at most 10 digits.

 

Example 1:

Input: sentence = "there are $1 $2 and 5$ candies in the shop", discount = 50

Output: "there are $0.50 $1.00 and 5$ candies in the shop"

Explanation: 
The words which represent prices are "$1" and "$2". 
- A 50% discount on "$1" yields "$0.50", so "$1" is replaced by "$0.50".
- A 50% discount on "$2" yields "$1". Since we need to have exactly 2 decimal places after a price, we replace "$2" with "$1.00".

Example 2:

Input: sentence = "1 2 $3 4 $5 $6 7 8$ $9 $10$", discount = 100

Output: "1 2 $0.00 4 $0.00 $0.00 7 8$ $0.00 $10$"

Explanation: 
Applying a 100% discount on any price will result in 0.
The words representing prices are "$3", "$5", "$6", and "$9".
Each of them is replaced by "$0.00".
'''

import string


def test(string1, discount):
   
    result = string.punctuation
    result= result.replace('$', ' ')
    
    a = string1.split(' ')
    for i in range(len(a)):
        if a[i] in result:
            continue
        elif a[i].isalnum():
            continue
        # elif up_alpha in i:
        #     continue
        else:
            if len(a[i]) > 1:
                l = a[i]
                if l[0] == '$':
                    k = l[1:]
                    if k.isdigit():
                        original_price = int(k)
                        if original_price > 0:
                            discount_price = original_price * (discount/100)
                            mayuri = original_price - discount_price
                            updated_value = str(mayuri)
                            k = l[0] + updated_value
                            a[i] = k
    string2 = ''
    test_str = ''
    for i in a:
        if string2 == test_str:
            string2 = string2 + i
        else:
            string2 = string2 + ' ' + i    
                
    return string2
    
    
# m = test("there are $1 $2 and 5$ candies in the shop", 50)
m = test("1 2 $3 4 $5 $6 7 8$ $9 $10$", 100)
print(m)