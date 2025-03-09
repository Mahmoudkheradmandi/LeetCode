'''
    تا استرینگ توش هستش  N ما یک تابع داریم که از ورودی یک لیست میگیرد که 
    از ما میخواهد که برنامه ای بنویسیم که طولانی ترین پیشوندی که در توی اون استرینگ ها است را پیدا کنیم 
    
    strs = ["flower","flow","flight"]
    Output: "fl"
    
'''

def longestCommonPrefix(strs):
    '''
        روش حل : اولین کاری میکنیم کوتاه ترین استرینگ رو پیدا میکنیم تا زیاد توش پیمایش نشود 
        یک پویتر اول استرینگ قرار میدیم تا زمانی که طول رشته اولی یا بقیه رشته ها تموم بشود 
        یکی یکی مقایسه میکنیم تا زمانی که حروف ها با هم یکی باشه 
        
    '''
    
    
    _str = min(strs) # پیدا کردن کوتاه‌ترین رشته در لیست
    for i in strs:
        j = 0
        while j < len(_str) and j < len(i):
           
            if _str[j] != i[j]:  # اگر کاراکترها متفاوت باشند، پیشوند مشترک را کوتاه می‌کنیم
                _str = _str[:j]
                break
            j += 1
        # اگر لیست خالی باشد 
        if not _str:
            break
    return _str
        
        
# روش پایتونی                 
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