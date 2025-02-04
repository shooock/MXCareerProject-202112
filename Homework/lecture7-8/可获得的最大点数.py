class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        # 滑动窗口大小为 n-k
        windowSize = n - k
        # 选前 n-k 个作为初始值
        s = sum(cardPoints[0:n-k])
        minSum = s
        for i in range(n-k, n):
            # 滑动窗口每向右移动一格，增加从右侧进入窗口的元素值，并减少从左侧离开窗口的元素值
            s += cardPoints[i] - cardPoints[i - n + k]
            minSum = min(minSum, s)
        return sum(cardPoints) - minSum