def myAtoi(s):
    # حذف فاصله‌های ابتدایی رشته
    s = s.lstrip()
    
    # طول رشته
    length = len(s)
    
    # اگر رشته خالی باشد، ۰ برمی‌گردانیم
    if not length:
        return 0
    
    # تعیین علامت عدد
    sign = 1
    i = 0
    
    # بررسی علامت + یا -
    if s[i] == '+':
        i += 1
    elif s[i] == '-':
        sign = -1
        i += 1
    
    # متغیر برای ذخیره نتیجه
    result = 0
    
    # حلقه برای تبدیل کاراکترهای عددی به عدد
    while i < length:
        cur = s[i]
        # اگر کاراکتر عددی نباشد، حلقه را می‌شکنیم
        if not cur.isdigit():
            break
        else:
            # اضافه کردن رقم به نتیجه
            result = result * 10 + int(cur)
        i += 1
    
    # اعمال علامت به نتیجه
    result *= sign
    
    # محدوده مجاز برای عدد
    INT_MIN = -2**31
    INT_MAX = 2**31 - 1
    
    # بررسی محدوده مجاز
    if result < INT_MIN:
        return INT_MIN
    elif result > INT_MAX:
        return INT_MAX
    
    # برگرداندن نتیجه نهایی
    return result

s = myAtoi("21474836460")
print (s)       
                