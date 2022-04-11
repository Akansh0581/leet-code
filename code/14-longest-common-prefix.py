# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common=strs[0]
        for i in range(1,len(strs)):
            for j in range(0,len(common)):
                if j>=len(strs[i]):
                    common=strs[i]
                    break
                elif common[j]!=strs[i][j]:
                    common=common[:j]
                    break
        return common
                
                