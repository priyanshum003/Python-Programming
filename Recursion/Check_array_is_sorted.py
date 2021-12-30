def arr_is_sorted(arr):
    l = len(arr)
    if l == 0 or l == 1:
        return True

    if arr[0] > arr[1]:
        return False

    smaller_list = arr_is_sorted(arr[1:])

    if smaller_list :
        return True
    else:
        return False


arr = [1,2,3,4,5]
print(arr_is_sorted(arr))