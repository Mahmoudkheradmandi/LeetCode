'''
    برعکس سوال قبلی ما حروف رومن رو عدد باید تبدیل کنیم 

'''

def romanToInt(s):
    
    '''
        روش حل : ما دیگه به حالت های خاص عدد های رومن نداریم 
        و این که چون میخواهیم حروف پیدا کنیم دیگه کلید های دیکشنری ما حروف ها  خواهند بود 
        یک پویتر به اول استرینگ 
        استرینگ اولی را با استرینگ بعدیش مقایسه میکنم 
        اگر کوچیک تر از بعدیش باشه  نگاه میکنم سیمبول چیه و تفریق میکنیم 
        اگر بزرگ بود جمع میکنیم 
        
        MCMXXIV = 
        M > C => +1000
        C < M => -100
        M > x => + 1000
        x = x => + 10
        x = x => +10 
        x > I => +10
        I < V => -1
        V => +5
        
        ==1934
        
    '''
    Symbol = {
        'M': 1000, 'D': 500, 'C': 100,
        'L': 50, 'X': 10, 'V': 5, 'I': 1
    }

    result = 0
    for i in range(len(s) - 1):
       
        if Symbol[s[i]] < Symbol[s[i + 1]]:  # اگر نماد فعلی کوچکتر از نماد بعدی باشد، آن را از نتیجه کم می‌کنیم
            result -= Symbol[s[i]]
        else:  # در غیر این صورت، آن را به نتیجه جمع می‌کنیم
            result += Symbol[s[i]]
            
    result += Symbol[s[-1]] # اضافه کردن مقدار آخرین نماد 
    return result         
    