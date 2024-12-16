def binary_search(arr, start, end, searched_element):
    while(start <= end):
        mid = (start + end) // 2
        if (arr[mid] == searched_element):
            return mid # Return the position where the element is
        elif(arr[mid] < searched_element):
            start = mid - 1
        else:
            end = mid - 1
    return -1

arr = [2, 3, 4, 10, 40]
searched_element = 40

# Call function
result = binary_search(arr, 0, len(arr)-1, searched_element)
if result != -1:
    print("Element is present at index", result)
else:
    print("Element is not present in array")