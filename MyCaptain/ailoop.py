def Positivenum(nums: list[int]) -> list[int]:
    posnum = []
    for x in nums:
        if x > 0:
            posnum.append(x)
        else:
            continue
    return(posnum)

print(Positivenum([12, -7, 5, 64, -14]))
print(Positivenum([12, 14, -95, 3]))