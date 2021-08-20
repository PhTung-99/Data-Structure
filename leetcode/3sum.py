def threeSum(a):
    res = set()
    a.sort()
    _set = set()
    for i in range(len(a)):
        if not(i > 2 and a[i] == a[i-2]): 
            for j in range(i+1, len(a)):
                sol = -(a[i]+a[j])
                if sol in _set:
                    res.add((a[i], a[j], sol))
            _set.add(a[i])
        else:
            print(i)
    print(list(res))

def test(a):
    res = set()
    a.sort()
    seen = set()
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            sol = -(a[i] + a[j])
            if sol in seen:
                res.add((a[i], a[j], sol))
        seen.add(a[i])
    print(res)
    

threeSum([-1,0,1,2,-1,-4,1,1,-1,-1,-1,-5,6])
test([-1,0,1,2,-1,-4,-1,-5,6])