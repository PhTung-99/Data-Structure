def insertionSort(a):
    # for i in range(len(arr)):
    #     j = i - 1
    #     while (arr[i] < arr[j] and j >= 0):
    #         arr[i], arr[j] = arr[j], arr[i]
    #         j -= 1
    #         i -= 1
    for i in range(len(a)):
            j = i -1
            while j >= 0 and a[i] <= a[j]:
                a[i], a[j] = a[j], a[i]
                i -= 1
                j -= 1

if __name__ == '__main__':
    arr = [4,1,2,5,8,2,123,1,52,2,1,43,3,2,23]
    print(arr)
    insertionSort(arr)
    print(arr)