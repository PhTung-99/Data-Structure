def partition(a, begin, end):
    privot = begin
    for i in range(begin + 1, end + 1):
        if (a[i] <= a[begin]):
            privot += 1
            a[i], a[privot] = a[privot], a[i]
    a[privot], a[begin] = a[begin], a[privot]
    return privot

def quickSort(a, begin = 0, end = None):
    if end is None:
        end = len(a) - 1
    def _quickSort(a, begin, end):
        if begin >= end:
            return
        privot = partition(a, begin, end)
        _quickSort(a, begin, privot-1)
        _quickSort(a, privot+1 , end)
    _quickSort(a, begin, end)
    
if __name__ == '__main__':
    arr = [5,2,1,7,9,3,4,0,5,10]
    quickSort(arr)
    print(arr)
