def longestCommonPrefix(strs):
    # پیدا کردن کوتاه‌ترین رشته در لیست
    _str = min(strs)
    
    # حلقه برای پیمایش تمام رشته‌ها
    for i in strs:
        j = 0
        # حلقه برای مقایسه کاراکترها
        while j < len(_str) and j < len(i):
            # اگر کاراکترها متفاوت باشند، پیشوند مشترک را کوتاه می‌کنیم
            if _str[j] != i[j]:
                _str = _str[:j]
                break
            j += 1
        # اگر پیشوند مشترک خالی باشد، حلقه را می‌شکنیم
        if not _str:
            break
    
    # برگرداندن پیشوند مشترک
    return _str
        
                
def longestCommonPrefix_2(strs):
    strs = sorted(strs)
    first = strs[0]
    last = strs[-1]
    for i in range(min(len(first) , len(last))): 
        if first[i] != last[i]: 
            return first[:i]
    return first   

strs = ["flower","flow","flight"]    
x = longestCommonPrefix(strs)
print(x) 