def fourSum(nums, target):
    # مرتب‌سازی لیست
    nums.sort()
    lst, quad = [], []
    
    # تابع بازگشتی برای پیدا کردن ترکیب‌های n‌تایی
    def n_sum(n, start, target):
        if n != 2:
            for i in range(start, len(nums) - n + 1):
                # جلوگیری از تکرار ترکیب‌ها
                if i > start and nums[i] == nums[i - 1]:
                    continue
                quad.append(nums[i])
                n_sum(n - 1, i + 1, target - nums[i])
                quad.pop()
            return
        
        # تعیین دو اشاره‌گر
        left, right = start, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] < target:
                left += 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                lst.append(quad + [nums[left], nums[right]])
                left += 1
                # جلوگیری از تکرار ترکیب‌ها
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
    
    n_sum(4, 0, target)
    return lst
                    
                        
        
