from typing import List 
def productExceptSelf(nums: List[int]) -> List[int]:
    prefix = []
    postfix = []
    result_arr = [None] * len(nums)
    print(result_arr)
    
    product = 1
    for i in range(0,len(nums)):
        product *= nums[i]
        prefix.append(product)
    
    product = 1
    for i in range(len(nums)-1, -1,-1):
        product *= nums[i]
        postfix.append(product)
    
    postfix = list(reversed(postfix))

    for i in range(0,len(nums)):
        # BEGINNING
        if i == 0:
            result_arr[i] = postfix[i+1]
        # END
        elif i == len(nums) - 1:
            result_arr[i] = prefix[i-1]
        # BETWEEN
        else:
            result_arr[i] = prefix[i-1] * postfix[i+1]

    return result_arr

nums = [1,2,3,4]
new_nums = [-1,1,0,-3,3]
print(productExceptSelf(new_nums))
