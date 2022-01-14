class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        total = 0
        # 没有技巧的时候顾客数量是
        for i in range(len(customers)):
            if grumpy[i]==0:
                total = total + customers[i]
        #当采用技巧后，第一组也就是increase0 是
        increase = 0
        for i in range(minutes):
            increase += customers[i]*grumpy[i]
        #滑动窗口，减去上一个，加上下一个求最大increase
        max_cus = increase
        for i in range(minutes,len(customers)):
            increase += customers[i]*grumpy[i] - customers[i-minutes]*grumpy[i-minutes]
            max_cus = max(max_cus,increase)
        return total+max_cus
