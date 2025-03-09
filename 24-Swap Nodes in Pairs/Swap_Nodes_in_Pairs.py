def swapPairs(head): 
    temp = ListNode(0 , head)
    pre = temp 
    while pre.next and pre.next.next :
        first = pre.next
        secand = pre.next.next
        pre.next = secand 
        first.next = secand.next
        secand.next = first
        pre = first
    return temp.next    