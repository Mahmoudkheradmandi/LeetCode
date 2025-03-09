def mergeKLists(self , lists):
    if not lists or len(lists)==0: 
        return None
    while len(lists) > 1 : 
        mergeList = []
        for i in range(0 , len(lists) , 2): 
            l1 = lists[i]
            l2 = lists[i +1] if i + 1 < len(lists) else None
            mergeList.append(self.mergeTowList(l1 , l2))
        lists = mergeList
    return lists[0]     
    
    
def mergeTowList(self ,l1 ,l2):
        temp = ListNode()
        cur = temp
        while l1 and l2 : 
            if l1.val < l2.val : 
                cur.next = l1
                l1 = l1.next 
            else : 
                cur.next = l2 
                l2 = l2.next 
            cur = cur.next
        if l1 : 
            cur.next = l1           
        else: 
            cur.next = l2
        return temp.next    
                