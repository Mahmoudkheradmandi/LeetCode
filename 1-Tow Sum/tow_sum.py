Number  = [3 ,7 ,4 ,1 ,8 ,2]
Target = 15

# The first method 
def two_Sum(number, target):
    length = len(Number)
    for i in range(length):
        val = Target - Number[i]
        for j in range(i+1 , length): 
            if Number[j] == val:
                return[i , j]
          
         
def twoSum(nums, target):
    
    '''
        : است instans دیکشنری سرعت دسترسی به خانه ها بیشتر است به خاطر این که 
        چون نوع داده هاش هش تیبل هستش 
        روش حل : یک عدد از لیست برمیداریم از تارگت کم میکنیم حاصل تفریق توی دیکشنری است یا نه 
        اگر هست : شماره خانه شمارنده و شماره خانه ی داخل دیکشنری را برمیگردانیم 
        اگر نبود: شمارنده را یکی  جلو میبریم 
    
    '''     
    _nums = {}
    length = len(nums)
    
    " در طول لیست خود اعداد را بیرون میکشیم و محاصبه میکنیم  "
    for i in range(length): 
        val = target - nums[i]
        
        if val in _nums: # چک میکنیم در دیکشنری وجود دارد یا نه 
            "اعداد رو برمیگردانیم index اگر بود اعداد رو برمیگردانیم  "
            " اگر نبود شمارنده را جلو ببر و عدد فعلی را در دیکشنری ذخیره کن "    
            return [i, _nums[val]]
        else:
            _nums[nums[i]] = i