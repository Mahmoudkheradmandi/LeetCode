def reverse(x):
    
    sign , x = (1 , x) if x >= 0 else(-1 , -x)
    result = 0 
    while x > 0 : 
        result = (result * 10) + (x % 10)
        x //= 10 
    result *= sign
    if result < -2**-31 and result > 2**31-1:
        return 0
    else: 
        return result        
    
x = reverse(1534236469)
print (x)    


def reverse_python(x):
        result = 0 
        if x < 0: 
            result = int(str(x)[1:][::-1])*-1
        else:
            result = int(str(x)[::-1])
        if result > 2 ** 31 -1 or result < -2 ** 31:
            return 0
        else: 
            return result          


