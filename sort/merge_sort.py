def mergeSort(arr):
    arr_len = len(arr)
    if arr_len > 1:
        mid = arr_len // 2
        firstArr = arr[:mid]
        secondArr = arr[mid:]
        mergeSort(firstArr)
        mergeSort(secondArr)
        i = j = k = 0
        while i < len(firstArr) and j < len(secondArr):
            if firstArr[i] < secondArr[j]:
                arr[k] = firstArr[i]
                i += 1
            else:
                arr[k] = secondArr[j] 
                j += 1
            k += 1
        while i < len(firstArr):
            arr[k] = firstArr[i]
            i += 1
            k += 1
 
        while j < len(secondArr):
            arr[k] = secondArr[j]
            j += 1
            k += 1


if __name__ == '__main__':
    arr = [4,1,2,3,5,6,4,23,65]
    print(arr)
    mergeSort(arr)
    print(arr)