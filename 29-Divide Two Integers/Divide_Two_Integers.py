def divide(self, dividend, divisor):
    
    if dividend == -2147483648 and divisor == -1:
        return 2147483647
    
    d = abs(dividend)
    dv = abs(divisor)
    q = 0
    
    while d >= dv:
        temp = dv
        mul = 1
        while d >= (temp << 1): 
            temp <<= 1
            mul <<= 1
        d -= temp
        q += mul
    

    if (dividend < 0) ^ (divisor < 0):
        q = -q
    
    if q > 2147483647:
        return 2147483647
    elif q < -2147483648: 
        return -2147483648
    else:
        return q
 