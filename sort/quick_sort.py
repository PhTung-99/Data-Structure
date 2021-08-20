def parition(a, low, high):
    i = low - 1
    privot = a[high]
    for j in range(low, high):
        if a[j] <= privot:
            i += 1
            a[j], a[i] = a[i], a[j]
    a[i+1], a[high] = a[high], a[i+1]
    return i + 1

def quickSort(a, low, high):
    if len(a) == 1:
        return 
    if low < high:
        i = parition(a, low, high)
        quickSort(a, low, i - 1)
        quickSort(a, i + 1, high)
  
  
# Driver code to test above
arr = [10, 7, 14, 9, 13]
n = len(arr)
quickSort(arr, 0, n-1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i])