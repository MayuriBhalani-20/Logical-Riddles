def bubble_sort(arr):
    length = len(arr)
    j = 0
    while j < length - 1:
        print(j)
        if (arr[j] **2 > arr[j + 1]):
            print("arr[j] --- ", arr[j])
            print("arr[j + 1] --- ", arr[j + 1])
            temp = arr[j] **2
            arr[j] = arr[j + 1] **2
            arr[j + 1] = temp  
            # arr[j] = arr[j] ** 2
            j = -1
            print("------------- ",j)
        else:
            print("-------- else - arr[j] --- ", arr[j])
            print("-------- else - arr[j + 1] --- ", arr[j + 1])
        j += 1
        print("------------- + ",j)
        print(f"\n\n----------- {j} -----------\n\n")

data = [-2, 0, 6, -8, 4]
print(data)

bubble_sort(data)
print(data)