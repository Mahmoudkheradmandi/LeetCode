def findMedianSortedArrays(nums1 , nums2):
    n1 = len(nums1)
    n2 = len(nums2)
    if n1 > n2 : 
        nums1 , nums2 = nums2 , nums1
        n1 , n2 = n2 , n1
    
    total_len = n1 + n2 
    half = total_len // 2 
    low , high = 0 , n1-1
    while True : 
        mid1 = (high + low) // 2
        mid2 = half - (mid1 + 1) -1
        
        mid_nums1 = nums1[mid1] if mid1 >= 0 else float('-infinity') # If my list is empty
        right_nums1 = nums1[mid1 + 1] if mid1 + 1 < n1 else float('infinity')
        mid_nums2 = nums2[mid2] if mid2 >= 0 else float('-infinity')
        right_nums2 = nums2[mid2 + 1] if mid2 + 1 < n2 else float('infinity')
    
        if mid_nums1 <= right_nums2 and mid_nums2 <= right_nums1: 
            
            if total_len % 2 == 1: 
                return min(right_nums1 , right_nums2)
            else : 
                return (max(mid_nums1 , mid_nums2) + min(right_nums1 , right_nums2)) / 2
        elif mid_nums1 > right_nums2 :
            high = mid1 - 1
        else :
            low = mid1 + 1  
     
     
            
def findMedianSortedArrays1(nums1 , nums2):
    nums1.extend(nums2)
    nums1  = sorted(nums1)
    
    length = len(nums1)
    if length % 2 : 
        return nums1[length // 2]
    else: 
        return (nums1[length // 2]+ nums2[length // 2-1]) / 2
                
            
                
                            