def isPalindrome(x):
    # اگر عدد منفی باشد، نمی‌تواند پالیندروم باشد
    if x < 0:
        return False
    
    # متغیر برای ذخیره عدد معکوس
    result = 0
    
    # کپی از عدد اصلی
    a = x
    
    # حلقه برای معکوس کردن عدد
    while a > 0:
        # اضافه کردن رقم آخر a به نتیجه
        result = result * 10 + a % 10
        # حذف رقم آخر از a
        a //= 10
    
    # بررسی آیا عدد معکوس شده با عدد اصلی برابر است
    return result == x


def isPalindromePython(x):
    s = str(x)
    return s == s[::-1]

   