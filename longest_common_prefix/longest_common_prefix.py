def longestCommonPrefix(strs):
        _str = min(strs)    
        for i in strs: 
            j = 0
            while j < len(_str) and j < len(i): 
                if _str[j] != i[j] : 
                    _str = _str[:j]
                j += 1
            return _str
        
                
def longestCommonPrefix_2(strs):
    strs = sorted(strs)
    first = strs[0]
    last = strs[-1]
    for i in range(min(len(first) , len(last))): 
        if first[i] != last[i]: 
            return first[:i]
    return first   

strs = ["flower","flow","flight"]    
x = longestCommonPrefix(strs)
print(x) 