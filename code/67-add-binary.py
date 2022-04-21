# Given two binary strings a and b, return their sum as a binary string.

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry,res,i=0,"",1
        if len(a)<len(b):a,b=b,a
        while i<=len(a):
            if i<=len(b):
                carry,rem=divmod((int(a[-1*i])+int(b[-1*i])+carry),2)
            else:
                carry,rem=divmod((int(a[-1*i])+carry),2)
            res=str(rem)+res
            i+=1
        return str(carry)+res if carry else res