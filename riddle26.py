'''
Given an array of strings words and an integer k, return the k most frequent strings.

Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.

 

Example 1:

Input: words = ["i","love","leetcode","i","love","coding"], k = 2
Output: ["i","love"]
Explanation: "i" and "love" are the two most frequent words.
Note that "i" comes before "love" due to a lower alphabetical order.
Example 2:

Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
Output: ["the","is","sunny","day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words, with the number of occurrence being 4, 3, 2 and 1 respectively.
'''


# a = ["i","love","leetcode","i","love","coding"]
a = ["the","day","is","sunny","the","the","the","sunny","is","is"]

def function(a, target):
    l1 = ['0' for i in range(len(a))]
    i = 0
    j = 1
    ans = []
    final_ans = []

    temp_dict = {}
    temp_word = ""
    count = 1
    while i < len(a):
        if a == l1:
            break
        else:
            temp_word = a[i]
            if a[i] == '0':
                    i = i+1
                    j = i+1
            elif j < len(a):
                
                if a[j] == '0':
                    j = j+1

                else:
                    temp_word = a[i]
                    if j < len(a):
                        if a[i] == a[j]:
                            a[j] = '0'
                            count = count + 1
                            j += 1
                        else:
                            j += 1
            else:
                temp_dict[temp_word] = count
                a[i] = '0'
                i = i+1
                j = i+1
                count = 1
    m = sorted(temp_dict.values())
    for i in m:
        if i <= target:
            ans.append(i)

    k = sorted(temp_dict.items())
    def get_key(val):
        for i in k:
            if i[1] == val:
                mayuri = i[0]
                # k = sorted(temp_dict.keys())
                k.remove(i)
                return mayuri
    n = 0
    while n < target:
        final_var = max(ans)
        ayush = get_key(final_var)
        final_ans.append(ayush)
        ans.remove(final_var)
        n = n+1
    
    return final_ans


print(function(a, 4))
