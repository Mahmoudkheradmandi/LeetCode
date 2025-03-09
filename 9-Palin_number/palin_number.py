'''
    یک عدد اینتیجر به ما میدهد که از هر طرف بخونیم همان عدد میشود
    مثلا ۱۲۱ از هر طرف بخونیم باز ۱۲۱ میشود 
    توجه باید بکنیم که اعداد  منفی پالیندروم ندارند
    اول باید برنامه را چک کنیم اگر منقی بود فالس برگردانیم 

'''

def isPalindrome(x):
    '''
        روش حل : به این صورت است که اول چک کنیم عدد منفی نباشد 
        و سپس برای این که عدد رو برعکس کنیم عدد رو تقسیم بر ۱۰ میکنیم و باقیمانده رو ضربدر ۱۰ میکنیم 
        تا زمانی که درگیر تقسیم نشود و همه را با هم جمع میکنیم 
        مثلا ۱۲۳ 
        
        ۱۲۳ / ۱۰ = ۱۲ باقیمانده => (۳) 
        ۱۲ / ۱۰ = ۲ باقیمانده => (۱) 
        ۱ / ۱۰ = - باقیمانده => (-) 
        
        (۳*۱۰) + ۲ = ۳۲
        ۳۲*۱۰ + ۱ = ۳۲۱‍
         
    '''
    if x < 0:   # اگر عدد منفی باشد، نمی‌تواند پالیندروم باشد
        return False
    result = 0
    a = x
    while a > 0:
        result = result * 10 + a % 10
        a //= 10
    return result == x



''' روش پایتونی '''

def isPalindromePython(x):
    s = str(x)
    return s == s[::-1]

   