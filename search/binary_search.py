def binary_search(arr, high, low , x):
    if high >= low:
        mid = (high + low ) // 2
        if arr[mid] == x:
            return mid
        elif x > arr[mid]:
            return binary_search(arr, high, mid + 1, x)
        else:
            return binary_search(arr, mid - 1, low, x )
    else:
        return None


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
    



arr = [ 2 ,3, 4, 10, 40 ]
x = 40   
result = binary_search(arr, len(arr)-1, 0, x)

if result:
    print(result)
