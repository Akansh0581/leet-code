# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

class Solution:
    def reverse(self, x: int) -> int:
        result=0
        negative=False
        if x<0:
            negative=True
            x=x*-1
        while x!=0:
            r=x%10
            x=int(x/10)
            result=(result*10)+r
        if negative:
            result=result*-1
        if result in range(-2**31,2**31-1):
            return result
        return 0
            
            