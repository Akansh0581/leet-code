# Given a non-negative integer x, compute and return the square root of x.

# Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

class Solution:
    def mySqrt(self, x: int) -> int:
        left,right=0,ceil(x/2)
        while left<=right:
            print(left,right)
            mid=int((left+right)/2)
            if mid**2 == x:return mid
            elif mid**2 > x:right=mid-1
            else:left=mid+1
        return left-1