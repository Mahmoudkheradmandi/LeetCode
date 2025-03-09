def generateParenthesis(n):
    result , stack = [] , []
    def back_tracker(op , cp): 
        if op == cp == n : 
            result.append(''.join(stack))
            return
        if op < n : 
            stack.append("(")
            back_tracker(op+1 , cp)
            stack.pop()
        if cp < op : 
            stack.append(")")
            back_tracker(op , cp+1)
            stack.pop()
    back_tracker(0 , 0)
    return result                
            