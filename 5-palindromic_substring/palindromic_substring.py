
'''  
    صورت سوال از ما میخواد که زیر مجموع استرینگ رو پیدا میکنیم و بعد باید از وسط نصف کنیم طوری که هر دو طرف با هم برابر باشد
    مثلا : aba => agar az b nesf konim a ba a brabar ast
    
'''

def longestPalindrome(s):
    
    '''
        روش حل : ما نیاز دارم به ۲ تا نشانه گر که از اولین نقطه شروع کنند 
        باید توجه داشته باشم که طول استرینگی که با ما داده میشود آیا فرد است یا زوج
        ما ۲ تا پویتر را روی ۲ تا کاراکتر اولی قرار میدهم 
        و چب و راست هم دیگر را مقایسه میکنیم 
        تا زمانی ادامه بدن که یا باهم برابر نباشند منظور چپ و راست هستش یا از استرینگ بیرون بزنن    
    
    '''
    
    n = len(s)
    if n == 0:  # اگر رشته خالی باشد، همان رشته خالی را برمی‌گردانیم
        return s
    result = ''
    result_length = 0  # طول طولانی‌ترین زیررشته پالیندروم
    
    
    for i in range(n):
       
        l, r = i, i
        # برای اعداد فرد
        while l >= 0 and r < n and s[l] == s[r]:
            # اگر طول زیررشته فعلی از طولانی‌ترین زیررشته بیشتر باشد، آن را به‌روزرسانی می‌کنیم
            if r - l + 1 > result_length:
                result = s[l:r+1]
                result_length = r - l + 1
            l -= 1
            r += 1
        
        # برای اعداد زوج
        l, r = i, i + 1
        while l >= 0 and r < n and s[l] == s[r]:
            if r - l + 1 > result_length:
                result = s[l:r+1]
                result_length = r - l + 1
            l -= 1
            r += 1
    
    # طولانی‌ترین زیررشته
    return result