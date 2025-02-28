
def convert(s, numRows):
    if numRows == 1: 
        return s
    
    m = [[] for i in range(numRows)]
    row , flag = 0 , True 
    for ch in s : 
        if flag : 
            m[row].append(ch)
            row += 1
        else : 
            row -= 1 
            m[row].append(ch)
        if row == numRows : 
            flag = not flag
            row -= 1
        elif row == 0 : 
            flag = not flag
            row +=1
    return ''.join([''.join(i) for i in m])                            
