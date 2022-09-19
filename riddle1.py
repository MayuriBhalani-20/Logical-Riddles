# Question: my input is [-2, 0, 4, -8, 6] and my output should be [0, 4, 16, 36, 64]-- The logic behind this is at first we have to square the elements of the list and then sort the list in assending order.

def square_function(array_list):
    # length1 = len(array_list)
    test_list = [1 for x in array_list]
    answer_list = [1 for x in array_list] # initializing answer list with same size of array_list with all elements equal to 1
    left_pointer = 0
    right_pointer = (len(array_list) - 1) # length of array - 1
    temp_pointer = (len(array_list) - 1) 

    while temp_pointer >= 0:
        if (answer_list == test_list):		
            if abs(array_list[left_pointer]) >= abs(array_list[right_pointer]):
                # abs means absolute value not considering sign(minus sign) of number 
                # above condition true if first element of array is larger
                answer_list[temp_pointer] = abs(array_list[left_pointer]) ** 2 # square of num
                left_pointer = left_pointer + 1 # increasing left pointer to 1 
            else:
                # it means right hand side element has larger absolute value
                answer_list[temp_pointer] = abs(array_list[right_pointer]) ** 2
                right_pointer = right_pointer - 1
        else:
            if abs(array_list[left_pointer]) >= abs(array_list[right_pointer]):
                if array_list[left_pointer] ** 2 <= answer_list[temp_pointer + 1]: 
                    answer_list[temp_pointer] = abs(array_list[left_pointer]) ** 2 # square of num
                    left_pointer = left_pointer + 1 # increasing left pointer to 1 
                else:
                    temp = array_list[left_pointer] ** 2
                    answer_list[temp_pointer] = answer_list[temp_pointer + 1]
                    answer_list[temp_pointer + 1] = temp
                    left_pointer = left_pointer + 1
            else:
                if array_list[right_pointer] ** 2 <= answer_list[temp_pointer + 1]: 
                    answer_list[temp_pointer] = abs(array_list[right_pointer]) ** 2
                    right_pointer = right_pointer - 1
                else:
                    temp = array_list[right_pointer] ** 2
                    answer_list[temp_pointer] = answer_list[temp_pointer + 1]
                    answer_list[temp_pointer + 1] = temp
                    right_pointer = right_pointer - 1
        temp_pointer = temp_pointer - 1

    return answer_list

l1 = [-2, 0, 4, -8, 6]
ans = square_function(l1)
print(ans)
