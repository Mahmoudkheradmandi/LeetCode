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


def twoSum(nums, target):
    # ایجاد یک دیکشنری برای ذخیره اعداد و اندیس‌های آن‌ها
    _nums = {}
    # طول لیست nums را محاسبه می‌کنیم
    length = len(nums)
    # حلقه برای پیمایش تمام عناصر لیست nums
    for i in range(length): 
        # مقدار مورد نیاز برای رسیدن به target را محاسبه می‌کنیم
        val = target - nums[i]
        # بررسی می‌کنیم که آیا این مقدار در دیکشنری وجود دارد یا نه
        if val in _nums:
            # اگر وجود داشت، اندیس‌های دو عددی که جمع آن‌ها برابر target است را برمی‌گردانیم
            return [i, _nums[val]]
        else:
            # اگر وجود نداشت، عدد فعلی و اندیس آن را در دیکشنری ذخیره می‌کنیم
            _nums[nums[i]] = i