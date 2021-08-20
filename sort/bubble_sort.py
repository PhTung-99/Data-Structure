def bubbleSort(a):
    # n = len(arr)
    # for i in range(n):
    #     for j in range(n-i-1):
    #         if (arr[j] > arr[j+1]):
    #             arr[j], arr[j+1] = arr[j+1], arr[j]
    n = len(a)
    for i in range(n):
        for j in range(n - i - 1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

if __name__ == '__main__':
    arr = [4,1,2,5,8,2]
    print(arr)
    bubbleSort(arr)
    print(arr)