def binary_search(arr, target, left, right):
    if left > right:

            mid = (left + right) // 2

    if arr[mid] == target:
        return mid
    
    elif arr[mid] < target:
        return binary_search(arr, target, left, mid + 1,)
    else:
        return binary_search(arr, target, mid - 1, right)

sorted_arr = [1, 3, 5, 7, 9, 11, 13, 15,]
print(binary_search(sorted_arr, 7, 0, len(sorted_arr) - 1))

