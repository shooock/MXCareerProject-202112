class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        yh = list()

        for i in range(numRows):
            nth_row = list()
            for j in range(i+1):
                if j == 0 or j == i:
                    ele = 1
                    nth_row.append(ele)
                else:
                    ele = yh[i-1][j-1]+yh[i-1][j]
                    nth_row.append(ele)
            yh.append(nth_row)
        return yh
