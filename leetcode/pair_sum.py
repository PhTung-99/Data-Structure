def check(nums):
    index = 1
    for i in range(1,len(nums)):
        if(nums[i-1]!=nums[i]):
            nums[index] = nums[i]
            index+=1
    return index
def check2(nums):
    index = 1
    for i in range(1,len(nums)):
        if(nums[i-1]!=nums[i]):
            nums[index] = nums[i]
            index+=1
    return index, nums
print(check([0,0,1,1,1,2,2,3,3,4]))
print(check2([3,2,2,3]))
