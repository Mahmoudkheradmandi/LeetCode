def myAtoi(s):
    s = s.lstrip()
    length = len(s)
    if not length : 
        return 0
    sign = 1 
    i = 0
    if s[i] == '+':
        i +=1
        print(s[i])
    elif s[i] == '-':
        sign = -1
        i += 1
        
    result = 0    
    while i < length :
        cur = s[i]
        if not cur.isdigit() :
            break
        else : 
            result = result*10 + int(cur)
        i += 1 
    result *= sign
    
    INT_MIN = -2**31
    INT_MAX = 2**31 - 1
    
    if result < INT_MIN: 
        return INT_MIN
    elif result > INT_MAX:
        return INT_MAX
    
    return result

s = myAtoi("21474836460")
print (s)       
                