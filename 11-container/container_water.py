
def maxArea(height):
    # دو اشاره‌گر برای شروع و پایان لیست
    left, right = 0, len(height) - 1
    
    # متغیر برای ذخیره بیشترین مقدار آب
    result = 0
    
    # حلقه تا زمانی که اشاره‌گرها به هم نرسیده‌اند
    while left < right:
        # محاسبه مساحت (آب) بین دو اشاره‌گر
        area = (right - left) * (min(height[left], height[right]))
        
        # اگر مساحت جدید بیشتر از مقدار قبلی باشد، آن را به‌روزرسانی می‌کنیم
        if area > result:
            result = area
        
        # حرکت اشاره‌گر با ارتفاع کمتر به سمت مرکز
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    # برگرداندن بیشترین مقدار آب
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
                          