def isPalindrome(x):
    if x < 0 : 
        return False
    result = 0
    a = x 
    while a > 0 : 
        result = result * 10 + a%10
        a //= 10
    return result == x 


def isPalindromePython(x):
    s = str(x)
    return s == s[::-1]

   