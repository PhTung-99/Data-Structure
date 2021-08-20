def mergeSort(a):
    if len(a) <= 1:
        return 
    mid = len(a) // 2
    left = a[:mid]
    right = a[mid:]
    mergeSort(left)
    mergeSort(right)
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            a[k] = left[i]
            i += 1
        else:
            a[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        a[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        a[k] = right[j]
        j += 1
        k += 1


if __name__ == '__main__':
    arr = [4,1,2,5,8,2]
    print(arr)
    mergeSort(arr)
    print(arr)
