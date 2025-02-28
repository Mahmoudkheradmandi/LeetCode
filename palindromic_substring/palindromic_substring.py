def longestPalindrome(s):
    n = len(s)
    if n == 0 : 
        return s
    result = ''
    result_length = 0
    for i in range(n):
        # for odd numbers
        l , r = i , i 
        while l >= 0 and r < n and s[l] == s[r] :
            if r-l+1 > result_length :
                result = s[l : r+1]
                result_length = r - l+1
            l -= 1
            r += 1
            
        # for even numbers
        l , r = i , i+1
        while  l >= 0 and r < n and s[l] == s[r] :
            if  r - l+1 > result_length : 
                result = s[l : r+1]
                result_length = r - l+1
            l -= 1
            r += 1    
    return result                     