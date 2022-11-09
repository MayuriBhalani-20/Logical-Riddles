'''
You are given a string num consisting of digits only.

Return the largest palindromic integer (in the form of a string) that can be formed using digits taken from num. It should not contain leading zeroes.

Notes:

You do not need to use all the digits of num, but you must use at least one digit.
The digits can be reordered.


Example 1:

Input: num = "444947137"
Output: "7449447"
Explanation: 
Use the digits "4449477" from "444947137" to form the palindromic integer "7449447".
It can be shown that "7449447" is the largest palindromic integer that can be formed.


Example 2:

Input: num = "00009"
Output: "9"
Explanation: 
It can be shown that "9" is the largest palindromic integer that can be formed.
Note that the integer returned should not contain leading zeroes.
'''
import numpy as np

def test(string1):
    list1 = []
    ans = ""
    for i in string1:
        list1.append(int(i))
    m = num_with_freq_dict(list1)
    key_of_m = list(m.keys())
    if 0 in key_of_m:
        del m[0]
    dict_2to9 = dict_with_2to9_numbers(m)
    dict_1 = dict_with_1_numbers(m)
    meet_values = list(dict_2to9.values())
    meet_keys = list(dict_2to9.keys())
    meet1_values = list(dict_1.values())
    meet1_keys = list(dict_1.keys())
    total_values = count_total_values(meet_values)
    for i in range(total_values):
        # a = max(meet_values)
        c = list(np.concatenate(meet_values))
        final = int(max(c))
        for i in range(len(meet_values)):
            if final in meet_values[i]:
                a = meet_values[i]
                break
        # final = max(a)
        position = meet_values.index(a)
        mom = meet_keys[position]
        if ans == "":
            if (mom == 2) or (mom == 4) or (mom == 6) or (mom == 8):
                for i in range(mom):
                    ans = ans + str(final)
                a.remove(final)
            else:
                if dict_1 == {}:
                    dict_1[1] = [final]
                else:
                    meet1_values[0].append(final)
                mom = mom - 1
                for i in range(mom):
                    ans = ans + str(final)
                a.remove(final)
        else:
            var1 = len(ans)//2
            # if (mom == 2) or (mom == 4) or (mom == 6) or (mom == 8):
            if mom in [2,4,6,8]:
                for i in range(mom):
                    ans = ans[:var1] + str(final) + ans[var1:]  
                a.remove(final)
            else:
                if dict_1 == {}:
                    dict_1[1] = [final]
                else:
                    meet1_values[0].append(final)
                mom = mom - 1
                for i in range(mom):
                    ans = ans[:var1] + str(final) + ans[var1:]  
                a.remove(final)
    if dict_1 == {}:
        pass
    else:
        meet1_values = list(dict_1.values())
        meet1_keys = list(dict_1.keys())
        a = max(meet1_values)
        final = max(a)
        position = meet1_values.index(a)
        mom = meet1_keys[position]  
        if ans == "":
            for i in range(mom):
                ans = ans + str(final)
            
        else:
            var1 = len(ans)//2
            for i in range(mom):
                ans = ans[:var1] + str(final) + ans[var1:]  
            
    return ans


def count_total_values(list1):
    count = 0
    for i in list1:
        for j in i:
            count = count + 1
    return count


def dict_with_1_numbers(dictionary):
    dict1 = {}
    values_list = dictionary.values()
    if 1 in values_list:
        a = [k for k,v in dictionary.items() if v == 1]
        dict1[1] = a
    return dict1    
    
    
def dict_with_2to9_numbers(dictionary):
    dict1 = {}
    values_list = dictionary.values()        
    if 2 in values_list:
        b = [k for k,v in dictionary.items() if v == 2]
        dict1[2] = b
    if 3 in values_list:
        c = [k for k,v in dictionary.items() if v == 3]
        dict1[3] = c
    if 4 in values_list:
        d = [k for k,v in dictionary.items() if v == 4]
        dict1[4] = d
    if 5 in values_list:
        e = [k for k,v in dictionary.items() if v == 5]
        dict1[5] = e
    if 6 in values_list:
        f = [k for k,v in dictionary.items() if v == 6]
        dict1[6] = f
    if 7 in values_list:
        g = [k for k,v in dictionary.items() if v == 7]
        dict1[7] = g
    if 8 in values_list:
        h = [k for k,v in dictionary.items() if v == 8]
        dict1[8] = h
    if 9 in values_list:
        i = [k for k,v in dictionary.items() if v == 9]
        dict1[9] = i
    
    return dict1 
    
            
def num_with_freq_dict(a):
    l1 = ['0' for i in range(len(a))]
    i = 0
    j = 1

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
    return temp_dict
    
# m = test("12346723464321")
# m = test("00009")
# m = test("444947137")
# m = test("8754329546234578")
# m = test("98766966789")                 # Mayuri's special case
m = test("3591024477898303119")                 # Mayuri's special case
print(m)


