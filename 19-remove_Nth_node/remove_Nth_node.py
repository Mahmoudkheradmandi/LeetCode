def removeNthFromEnd(head, n: int):
    # ایجاد یک نود موقت
    temp = ListNode(0, head)
    current, pre = head, temp
    
    # حرکت به سمت جلو برای پیدا کردن نود n‌ام از انتها
    while current and n:
        current = current.next
        n -= 1
    
    # حرکت به سمت جلو تا انتهای لیست
    while current:
        current = current.next
        pre = pre.next
    
    # حذف نود n‌ام از انتها
    pre.next = pre.next.next
    return temp.next