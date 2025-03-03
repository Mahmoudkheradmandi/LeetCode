def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    # جمع مقادیر اولیه دو گره اول از لیست‌های l1 و l2
    val = l1.val + l2.val
    
    # ایجاد گره اولیه برای نتیجه با مقدار یکان جمع (val % 10)
    result = ListNode(val % 10)
    
    # محاسبه رقم نقلی (carry) برای جمع بعدی
    carry = val // 10
    
    # ایجاد یک اشاره‌گر موقت برای حرکت در لیست نتیجه
    temp = result
    
    # حرکت به گره‌های بعدی در لیست‌های l1 و l2
    l1, l2 = l1.next, l2.next
    
    # حلقه تا زمانی که یکی از لیست‌ها یا رقم نقلی (carry) باقی مانده باشد
    while l1 or l2 or carry:
        # مقدار گره فعلی l1 (اگر وجود داشته باشد، در غیر این صورت 0)
        v1 = l1.val if l1 else 0
        
        # مقدار گره فعلی l2 (اگر وجود داشته باشد، در غیر این صورت 0)
        v2 = l2.val if l2 else 0
        
        # جمع مقادیر گره‌ها و رقم نقلی
        val = v1 + v2 + carry
        
        # ایجاد گره جدید در لیست نتیجه با مقدار یکان جمع (val % 10)
        temp.next = ListNode(val % 10)
        
        # حرکت به گره بعدی در لیست نتیجه
        temp = temp.next
        
        # محاسبه رقم نقلی جدید برای جمع بعدی
        carry = val // 10
        
        # حرکت به گره‌های بعدی در لیست‌های l1 و l2 (اگر وجود داشته باشند)
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    
    # برگرداندن لیست نتیجه
    return result

 