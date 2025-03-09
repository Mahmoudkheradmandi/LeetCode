
def findMedianSortedArrays(nums1, nums2):
    # طول آرایه‌ها را محاسبه می‌کنیم
    n1 = len(nums1)
    n2 = len(nums2)
    
    # اگر طول nums1 از nums2 بیشتر باشد، جای آن‌ها را عوض می‌کنیم
    if n1 > n2:
        nums1, nums2 = nums2, nums1
        n1, n2 = n2, n1
    
    # طول کل دو آرایه
    total_len = n1 + n2
    
    # نصف طول کل
    half = total_len // 2
    
    # محدوده جستجو در nums1
    low, high = 0, n1 - 1
    
    # حلقه بی‌نهایت تا زمانی که میانه پیدا شود
    while True:
        # وسط nums1 را پیدا می‌کنیم
        mid1 = (high + low) // 2
        
        # وسط nums2 را بر اساس mid1 محاسبه می‌کنیم
        mid2 = half - (mid1 + 1) - 1
        
        # مقدار وسط nums1 (اگر وجود نداشته باشد، منفی بی‌نهایت)
        mid_nums1 = nums1[mid1] if mid1 >= 0 else float('-inf')
        
        # مقدار بعد از وسط nums1 (اگر وجود نداشته باشد، مثبت بی‌نهایت)
        right_nums1 = nums1[mid1 + 1] if mid1 + 1 < n1 else float('inf')
        
        # مقدار وسط nums2 (اگر وجود نداشته باشد، منفی بی‌نهایت)
        mid_nums2 = nums2[mid2] if mid2 >= 0 else float('-inf')
        
        # مقدار بعد از وسط nums2 (اگر وجود نداشته باشد، مثبت بی‌نهایت)
        right_nums2 = nums2[mid2 + 1] if mid2 + 1 < n2 else float('inf')
        
        # اگر شرط پیدا شدن میانه برقرار باشد
        if mid_nums1 <= right_nums2 and mid_nums2 <= right_nums1:
            # اگر طول کل فرد باشد، میانه برابر کوچک‌ترین مقدار بعد از وسط است
            if total_len % 2 == 1:
                return min(right_nums1, right_nums2)
            # اگر طول کل زوج باشد، میانه برابر میانگین دو مقدار وسط است
            else:
                return (max(mid_nums1, mid_nums2) + min(right_nums1, right_nums2)) / 2
        # اگر وسط nums1 بزرگ‌تر از مقدار بعد از وسط nums2 باشد، جستجو در نیمه پایین nums1 ادامه می‌یابد
        elif mid_nums1 > right_nums2:
            high = mid1 - 1
        # در غیر این صورت، جستجو در نیمه بالای nums1 ادامه می‌یابد
        else:
            low = mid1 + 1
             
     
     
            
def findMedianSortedArrays1(nums1 , nums2):
    nums1.extend(nums2)
    nums1  = sorted(nums1)
    
    length = len(nums1)
    if length % 2 : 
        return nums1[length // 2]
    else: 
        return (nums1[length // 2]+ nums2[length // 2-1]) / 2
                
            
                
                            