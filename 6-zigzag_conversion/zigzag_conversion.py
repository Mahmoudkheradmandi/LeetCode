def convert(s, numRows):
    # اگر تعداد ردیف‌ها ۱ باشد، همان رشته را برمی‌گردانیم
    if numRows == 1:
        return s
    
    # ایجاد یک لیست از لیست‌ها برای ذخیره کاراکترها در هر ردیف
    m = [[] for i in range(numRows)]
    
    # متغیرهای برای ردیف فعلی و جهت حرکت
    row, flag = 0, True
    
    # حلقه برای پیمایش تمام کاراکترهای رشته
    for ch in s:
        # اگر جهت حرکت به سمت پایین باشد
        if flag:
            m[row].append(ch)
            row += 1
        # اگر جهت حرکت به سمت بالا باشد
        else:
            row -= 1
            m[row].append(ch)
        
        # اگر به آخرین ردیف رسیده باشیم، جهت حرکت را تغییر می‌دهیم
        if row == numRows:
            flag = not flag
            row -= 1
        # اگر به اولین ردیف رسیده باشیم، جهت حرکت را تغییر می‌دهیم
        elif row == 0:
            flag = not flag
            row += 1
    
    # ترکیب کاراکترها از لیست‌ها و برگرداندن نتیجه نهایی
    return ''.join([''.join(i) for i in m])          
