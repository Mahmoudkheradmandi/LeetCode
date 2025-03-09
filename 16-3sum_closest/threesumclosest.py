'''
    مثل سوال قبل هستش ولی این جا یک ورودی تارکت ها داریم 
    باید مجموع اعدادی را پیدا کنیم که به تارگت نزدیک  باشند 
    
'''


def threeSumClosest(nums, target):
    
    '''
        روش حل : مانند سوال قبلی هستش البته میتونیم این سوال رو با توابع برگشتی هم بنوسیم 
        مانند سوال قبلی ما به ۳ تا اشاره گر نیاز داریم 
        که به همان شکل شروع شوند و تمام شوند
        نکته ی سوال این بخش هستش که ما به جای صفر با تارگت مقایسه میکنیم 
        دوم : در ابتدا باید برای این که مجموع تمامی حالت ها رو به دست بیاریم باید از منفی بینهایت استفاده کنیم
        فقط در مرحله ی اول لازم است 
        
    '''
    
    
    nums.sort()
    length = len(nums)
    closest = float('-inf')
      
    for i in range(length - 2): # جلوگیری از تکرار 
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, length - 1

        while left < right:
            current = nums[i] + nums[left] + nums[right] 
            
            if current == target:
                return target
            
            if abs(current - target) < abs(closest - target): # اگر مجموع به هدف نزدیک‌تر باشد، آن را ذخیره می‌کنیم
                closest = current
            elif current < target: # اگر مجموع کمتر از هدف باشد، اشاره‌گر چپ را افزایش می‌دهیم
                left += 1
            else: # اگر مجموع بیشتر از هدف باشد، اشاره‌گر راست را کاهش می‌دهیم
                right -= 1 
    return closest


nums = [3 , -1 , 2, 9 , 1]
x = threeSumClosest(nums , 4)
print(x)


