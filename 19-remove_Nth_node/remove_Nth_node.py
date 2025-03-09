def removeNthFromEnd(head, n: int):
    
    # اول به ابتدای لینک لیست ها به نود جدید اضافه میکنیم 
    # به این دلیل که اگر ما تنها یک نود داده باشند الگوریتم ما کار کند 
    # برای حل این مسئله ما به ۳ تا متغییر نیاز داریم 
    
    temp = ListNode(0, head)
    current, pre = head, temp
    
    # جلو میبریم  n کارنت را تا خانه ی 
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