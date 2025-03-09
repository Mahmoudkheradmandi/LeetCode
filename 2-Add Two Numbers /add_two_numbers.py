

'''
سوال به ما ۲ تا لینک لیست میدهد ما باید این ۲ تا لینک لیست رو با هم جمع کنیم و حاصل جواب را به صورت لینک لیست برگردانیم  
    
'''
def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    
    '''
        است (carry) روش حل : مانند جمع معمولی هستش فقط مشکل باقیمانده جمع را داریم که همان 
        که با تقسیم اعداد میتوانیم به دست بیاریم  
        مثلا ۱۲ / ۱۰ حاصل باقیمانده ۲ میشود و کری میشود یک 
        را جلو میبریم  temp ذخیره میکنم اگر کری داشته باشه در کری و  result حالا جواب را در 
        در نهایت هم طول لینک لیست ها باید تمام بشود و هم کری صفر بشود 
        
    '''
    
    val = l1.val + l2.val
    result = ListNode(val % 10)    
    carry = val // 10
    temp = result # ایجاد یک اشاره گر 
    l1, l2 = l1.next, l2.next
    

    while l1 or l2 or carry:
        ''' 
        احتمال دارد طول لینک لیست ها
        برابر نباشد یکی ۴ رقمی و دیگری ۲ رقمی میگیم زمانی که به انتها رسیدی
        ولی اون یکی لینک لیست تمام نشده بود به جای جای خالی صفر قرار بده  

        '''
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0
        val = v1 + v2 + carry
        temp.next = ListNode(val % 10)
        temp = temp.next
        carry = val // 10
        
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    
    return result

 