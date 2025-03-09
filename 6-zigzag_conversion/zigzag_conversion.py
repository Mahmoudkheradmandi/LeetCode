""" یک استرینگ میدهد ما باید با پترن زیگزاگ بنوسیم و در آخر به صورت خطی بخونیم  """

def convert(s, numRows):
    
    """ 
        یک استرینگ میدهد ما باید با پترن زیگزاگ بنوسیم و در آخر به صورت خطی بخونیم  
        یه تعداد لیست درست میکنیم  numRows ما اول نسبت به   
        یک پویتر میسازیم و اول استرینگ  قرار میذهیم 
        
    """


    if numRows == 1:
        return s
    m = [[] for i in range(numRows)]
    
    # بود ما به سمت پایین میرویم و اگر نبود م به سمت بالا میرویم  True flag اگر 
    # علامتش برعکس بشه flag مشخص میکند که کی این row  
    # در واقع شمارههه ی لیست که قرار است در آن استرینگ قرار بگیره را نمایش میدهد  row
    # را عوض میکند و به سمت بالا میرود flag و زمانی که به اخرین لیست برسه علامت 
    row, flag = 0, True 
    

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
    
    return ''.join([''.join(i) for i in m])          
