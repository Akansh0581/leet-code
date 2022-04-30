# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pascal=[[1]]
        for i in range(1, rowIndex+1):
            pascal.append(list(map(lambda x,y:x+y, [0]+pascal[i-1],pascal[i-1]+[0])))
        return pascal[-1]