def threeSum(nums):
    # مرتب‌سازی لیست
    nums.sort()
    length = len(nums)
    out = []
    
    # حلقه برای پیمایش لیست
    for i in range(length - 2):
        # جلوگیری از تکرار ترکیب‌ها
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        # تعیین دو اشاره‌گر
        left, right = i + 1, length - 1
        
        # حلقه برای پیدا کردن ترکیب‌های سه‌تایی
        while left < right:
            current = nums[i] + nums[left] + nums[right]
            
            # اگر مجموع صفر باشد، ترکیب را ذخیره می‌کنیم
            if current == 0:
                out.append([nums[i], nums[left], nums[right]])
                # جلوگیری از تکرار ترکیب‌ها
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            # اگر مجموع کمتر از صفر باشد، اشاره‌گر چپ را افزایش می‌دهیم
            elif current < 0:
                left += 1
            # اگر مجموع بیشتر از صفر باشد، اشاره‌گر راست را کاهش می‌دهیم
            else:
                right -= 1
                
    return out