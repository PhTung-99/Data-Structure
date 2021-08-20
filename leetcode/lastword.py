def length(s):
    a = s.split()
    if(len(a)<=0):
        return 0
    else:
        return len(a[-1])

print(length("Hello World"))