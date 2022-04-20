# Given a string s consisting of some words separated by some number of spaces, return the length of the last word in the string.

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        try:
            s=s.strip()
            n=len(s)-s.rindex(" ")-1
        except ValueError:
            return len(s)
        return n