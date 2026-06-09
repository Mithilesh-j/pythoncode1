def multi(*nums):
    t=1
    for i in nums:
        t*=i
    return t


print(multi(2,3,4,5))
