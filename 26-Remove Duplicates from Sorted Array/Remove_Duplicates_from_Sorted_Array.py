def removeDuplicates(nums):
    i = 1 
    if len(nums) > 1 : 
        while i < len(nums): 
            if nums[i] == nums[i-1]:
                nums.pop(i)
            else: 
                i += 1
    return i                 