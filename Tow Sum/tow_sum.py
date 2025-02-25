Number  = [3 ,7 ,4 ,1 ,8 ,2]
Target = 15

# The first method 
def two_Sum(number, target):
    length = len(Number)
    for i in range(length):
        val = Target - Number[i]
        for j in range(i+1 , length): 
            if Number[j] == val:
                return[i , j]
      
x = two_Sum(Number , Target)
print(x) 
 
def twoSum(nums, target):
    _nums = {}
    length = len(nums)
    for i in range(length): 
        val = target - nums[i]
        if val in _nums:
            return [i , _nums[val]]
        else:
            _nums[nums[i]] = i
            
x = twoSum(Number , Target)
print(x)            