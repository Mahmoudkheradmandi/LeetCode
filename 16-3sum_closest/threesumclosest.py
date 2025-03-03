def threeSumClosest(nums, target):
    # مرتب‌سازی لیست
    nums.sort()
    length = len(nums)
    closest = float('-inf')
   
   
    for i in range(length - 2):
        # جلوگیری از تکرار ترکیب‌ها
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        # تعیین دو اشاره‌گر
        left, right = i + 1, length - 1
        # حلقه برای پیدا کردن ترکیب‌های سه‌تایی
        while left < right:
            current = nums[i] + nums[left] + nums[right] 
            
            if current == target:
                return target
            # اگر مجموع به هدف نزدیک‌تر باشد، آن را ذخیره می‌کنیم
            if abs(current - target) < abs(closest - target):
                closest = current
            # اگر مجموع کمتر از هدف باشد، اشاره‌گر چپ را افزایش می‌دهیم
            elif current < target:
                left += 1
            # اگر مجموع بیشتر از هدف باشد، اشاره‌گر راست را کاهش می‌دهیم
            else:
                right -= 1
                
    return closest


nums = [3 , -1 , 2, 9 , 1]
x = threeSumClosest(nums , 4)
print(x)


