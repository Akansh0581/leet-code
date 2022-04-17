# Implement strStr().

# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Clarification:

# What should we return when needle is an empty string? This is a great question to ask during an interview.

# For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle=="":return 0
        for i in range(0,len(haystack)-len(needle)+1):
            found=True
            for j in range(0,len(needle)):
                if needle[j]!=haystack[i+j]:
                    found=False
            if found: return i
        return -1
            
                            