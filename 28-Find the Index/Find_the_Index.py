def strStr(self, haystack ,needle):
     
     return haystack.index(needle) if needle in haystack else -1
 
 
def strStr_2(self, haystack ,needle): 
    
    if needle == haystack : 
        return 0
    for i in range(len(haystack) - len(needle) + 1): 
        if needle == haystack[i : i+len(needle)]: 
            return i
    return -1    
 