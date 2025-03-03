def letterCombinations(digits):
    
    # روش حال با تابع برگشتی 

    letter = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
              '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    
    combinations = []
    
    # تابع بازگشتی 
    def back_traker(i, curstr):
        # زمانی برنامه ی ما تمام میشود 
        if len(curstr) == len(digits):
            combinations.append(curstr)
            return
        # آیتم های داخل لیستی که داده شده را دیکشتری ما مقایسه میکند تا زمانی که آیتم ها به اتمام برسد 
        # به صورت درختی هر آیتمی که در داخل لیست داده شده است را با دیکشنری مقایسه میکند
        # اکر داخل دیکشنری باشد ولیوو های دیکشنری را بیرون میکشد
        # اضافه میکند combinations در نهایت ولیوو های دیکشتری را کنار هم قرار میدهد و به لیست 
        for c in letter[digits[i]]:
            back_traker(i + 1, curstr + c)
    
    if digits:
        back_traker(0, '')
    return combinations       
         