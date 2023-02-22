def insert(nums, num):
    start = 0
    end = len(nums)
    while start + 2 < end:
        midIdx = int(start + end / 2)
        if nums[midIdx] > num:
            end = midIdx + 1
        elif nums[midIdx] <  num:
            start = midIdx
        else:
            nums.insert(midIdx + 1, num)
            return nums
            
    if nums[midIdx] > num:
        if nums[start] >= num:
            nums.insert(start, num)
        else:
            nums.insert(midIdx, num)
    elif nums[midIdx] < num:
        if nums[end] <= num:
            nums.append(num)
        else:
            nums.insert(midIdx + 1, num)
    return nums


sorted = [7, 8, 11, 12, 14, 16, 17]
sorted = insert(sorted, 12)
