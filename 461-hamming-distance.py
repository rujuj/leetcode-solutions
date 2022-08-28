class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        bx = str(bin(x))[2:]
        by = str(bin(y))[2:]
        count = 0
        
        for x in range(len(by) - len(bx)):
            bx = "0" + bx
        for x in range(len(bx) - len(by)):
            by = "0" + by
        
        for i in range(len(bx)):
            if bx[i] != by[i]:
                count += 1
        
        return count