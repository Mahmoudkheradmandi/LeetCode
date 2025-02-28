def maxArea(height):
    left , right = 0 , len(height)-1
    result = 0
    while left < right :
        area = (right - left) * (min(height[left] , height[right]))
        if area > result : 
            result = area
        if height[left] < height[right]: 
            left += 1
        else: 
            right -= 1
    return result                
             
def maxArea_2(height):
    m = max(height)
    left , right = 0 , len(height)-1
    result = 0
    while left < right :
        area = (right - left) * (min(height[left] , height[right]))
        if area > result : 
            result = area
        if height[left] < height[right]: 
            left += 1
        else: 
            right -= 1
        if result > (right - left) * m : 
            break    
    return result                
                          