def nextPermutation(self, nums):
    """
        Do not return anything, modify nums in-place instead.
    """
    length = len(nums)
    if length <= 2 : 
        nums.reverse()
        return 
    pick = length -1
    while pick > 0 and nums[pick] <= nums[pick-1]: 
        pick -= 1
    if pick == 0 : 
        nums.reverse()
        return
    i = last = pick
    n = nums[pick - 1]
    while i < length : 
        if n < nums[i] and nums[i] < nums[last]: 
            last = i
        i += 1
    nums[pick - 1] , nums[last] = nums[last] , nums[pick - 1]
    nums[pick:] = sorted(nums[pick:])            
    