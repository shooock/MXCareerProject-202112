class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        dp=[nums[0]]
        last=-1
        mm=1000000
        for i in range(1,len(nums)):
            if nums[i]<dp[-1]:
                last=i
                mm=min(mm,nums[i])
            else:
                dp.append(nums[i])
        if last==-1:
            return 0
        for i in range(len(nums)):
            if nums[i]>mm:
                return last-i+1