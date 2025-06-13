def check_and_reverse(arr):
    n=len(arr)
    first_half_sum=sum(arr[:n//2])
    second_half_sum=sum(arr[n//2:])
    
    if first_half_sum < second_half_sum:
        arr.reverse()
        
    print(arr)
    
arr=[1,2,3,10,20,30]
check_and_reverse(arr)