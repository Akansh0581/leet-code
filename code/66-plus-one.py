# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry,n=0,len(digits)-1
        digits[-1]+=1
        while n>=0:
            if digits[n]+carry>9:
                carry,digits[n]=divmod(digits[n]+carry,10)
            else:
                carry,digits[n]=0,digits[n]+carry
            n-=1
            if not carry:break
        if carry>0:digits.insert(0,carry)
        return digits
                
