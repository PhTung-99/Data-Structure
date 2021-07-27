s = "eyndkzgaldjoujyvdpnfnjwijyuqslzwkcfgwass"
number = 0
for i in s:
    temp = ord(i) - 96
    if temp >= 10:
        number = number * 100 +temp
    else:
        number = number * 10 +temp
count = 0
a = [int(x) for x in str(number)]
k=1
while count < k:
    a = sum([int(x) for x in str(number)])
    number = a
    count +=1
print(a)

