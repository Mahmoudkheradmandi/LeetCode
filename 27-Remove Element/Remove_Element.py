def removeElement(self, nums ,val):
    x = 0 
    for i in range(len(nums)):
        if nums[i] != val:
            nums[i] , nums[x] = nums[x] , nums[i]
            x += 1
        return x
        
             
    