class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        vis =set([(0,0)])
        for i in range(m):
            for j in range(n):
                if i//10 +i%10 +j//10+j%10 <= k and ((i-1,j) in vis or (i,j-1) in vis):
                    vis.add((i,j))
        return len(vis)