def lengthOfLongestSubstring(self, s: str) -> int:
    _set = set()
    i = j = 0
    length , _max = (0 , 0)if len(s) else(len(s) , 0)
    while j < length : 
        if s[j] not in _set: 
            _set.add(s[j])
            if _max <= j-i : 
                _max = j - i +1
            j += 1 
        else : 
            _set.remove(s[i])
            i += 1
    return _max                 