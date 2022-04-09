# Given an integer x, return true if x is palindrome integer.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x<0 or x%10==0) and x!=0: return False 
        rev=0
        while x>rev:
            x,r=divmod(x,10)
            rev=rev*10+r
        return x==rev or x==int(rev/10)
            
        