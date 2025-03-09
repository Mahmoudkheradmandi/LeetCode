def reverseKGroup(self ,head, k):
    count = 0 
    temp = head
    while temp and count < k : 
        temp = temp.next
        count += 1 
    if count < k : 
        return head
    pre , cur = None , head
    for i in range(k): 
        nxt = cur.next
        cur.next = pre
        pre = cur
        cur = nxt
    if cur : 
        head.next = self.reverseKGroup(cur , k)
    return pre               