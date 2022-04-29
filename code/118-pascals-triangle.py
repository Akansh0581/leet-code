# Given an integer numRows, return the first numRows of Pascal's triangle.

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal=[None]*numRows
        for i in range(0,numRows):
            line=[None]*(i+1)
            line[0],line[-1]=1,1
            for j in range(1,i):
                line[j]=pascal[i-1][j-1]+pascal[i-1][j]
            pascal[i]=line
            i+=1
        return pascal
            
            