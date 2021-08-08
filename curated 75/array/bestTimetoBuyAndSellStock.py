from typing import *
import sys

def maxProfit(prices: List[int]) -> int:
    minPrice = sys.maxsize
    maxProfit = 0

    for n in prices:
        if n < minPrice:
            minPrice = n
        elif n - minPrice > maxProfit:
            maxProfit = n - minPrice
    
    return maxProfit

arr = [7,1,5,3,6,4]
print(maxProfit(arr))