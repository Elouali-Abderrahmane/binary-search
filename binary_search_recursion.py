def binary_search_recursion(arr, start, end, searched_element):
    if (start <= end):
        mid = (start + end) // 2

        if (arr[mid] == searched_element):
            return mid
        elif (arr[mid] < searched_element):
            return binary_search_recursion(arr, mid + 1, end, searched_element)
        else:
            return binary_search_recursion(arr, start, mid - 1, searched_element)
    else: 
        return -1

arr = [2, 3, 4, 10, 40]
searched_element = 40

# Call function
result = binary_search_recursion(arr, 0, len(arr)-1, searched_element)
if result != -1:
    print("Element is present at index", result)
else:
    print("Element is not present in array")