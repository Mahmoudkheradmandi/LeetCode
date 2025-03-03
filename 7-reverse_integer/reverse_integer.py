def reverse(x):
    # تعیین علامت عدد و تبدیل آن به مقدار مثبت
    sign, x = (1, x) if x >= 0 else (-1, -x)
    
    # متغیر برای ذخیره نتیجه معکوس
    result = 0
    
    # حلقه برای معکوس کردن عدد
    while x > 0:
        # اضافه کردن رقم آخر x به نتیجه
        result = (result * 10) + (x % 10)
        # حذف رقم آخر از x
        x //= 10
    
    # اعمال علامت به نتیجه
    result *= sign
    
    # بررسی محدوده مجاز برای عدد معکوس شده
    if result < -2**31 or result > 2**31 - 1:
        return 0
    else:
        return result     
    
x = reverse(1534236469)
print (x)    


def reverse_python(x):
        result = 0 
        if x < 0: 
            result = int(str(x)[1:][::-1])*-1
        else:
            result = int(str(x)[::-1])
        if result > 2 ** 31 -1 or result < -2 ** 31:
            return 0
        else: 
            return result          


