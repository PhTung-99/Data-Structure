def binary_search(arr, high, low , x):
    # if high >= low:
    #     mid = (high + low ) // 2
    #     if arr[mid] == x:
    #         return mid
    #     elif x > arr[mid]:
    #         return binary_search(arr, high, mid + 1, x)
    #     else:
    #         return binary_search(arr, mid - 1, low, x )
    # else:
    #     return None
    if low > high:
            return high+1
    mid = (high + low) //2 
    if arr[mid] == x:
        return mid
    elif arr[mid] > x:
        return binary_search(arr, mid - 1, low, x)
    else: 
        return binary_search(arr, high, mid + 1,x)



def binary_search_while(arr, x):
    low = 0 
    high = len(arr) - 1   
    mid = 0
    while low <= high:
        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    



arr = [1,3,5,6]
x = 2
result = binary_search(arr, len(arr)-1, 0, x)

print(result)
