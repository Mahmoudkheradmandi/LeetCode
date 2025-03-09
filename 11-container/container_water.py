'''
    صورت سوال میگه ما یک سری ستون داریم که این ها یک سری ارتفاع دارند
    ما باید ۲ تا ستون رو پیدا کنیم که اگر بین این ۲ تا ستون ما اب بریزیم بیشترین حجم آب جمع بشه 

'''

def maxArea(height):
    
    '''
        روش حل : ۲ تا پوینتر نیاز داریم که یکی از اول شروع کنه یکی از آخر لیست 
        با زمانی ادامه داشته باشد که این دو تا پویتر به هم نرسند
        کاری که میکنیم ما مساحت بین این دو نقطه رو پیدا میکنیم 
        مانند مساحت مسطیل 
        فقط باید توجه کنیم که این ستون های مینیموم رو انتخاب کنیم 
        تا حداقل ها رو با هم بررسی کنیم . حداقل مساحت هر کدام بیشتر باشه تون ۲ تا ستون رو انتخاب میکنیم 
        نکته جواب این است که مساحت را پیدا میکنیم و بعد نگاه میکنیم که ارتفاع ستون کدام طرف کمتر است چپ یا راست 
        هر کدام کمتر بود پویتر اون بخش را یکی به جلو اضافه میکنیم 
        
    '''
    

    left, right = 0, len(height) - 1
    result = 0
    while left < right:
        #  مساحت
        area = (right - left) * (min(height[left], height[right])) 
        if area > result: # اگر مساحت جدید بیشتر از مقدار قبلی باشد، آن را به‌روزرسانی می‌کنیم
            result = area
        # حرکت اشاره‌گر با ارتفاع کمتر به سمت مرکز
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
                          