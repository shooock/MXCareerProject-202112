class Solution:
    #判断条件要写在前面，迭代条件要写在后面，注意条件的顺序
    def restoreIpAddresses(self, s: str) -> List[str]:
        seg_count = 4
        ans = list()
        segment = [0]*4
        def dfs(segId: int, segStart: int):
            if segId == seg_count:
                if segStart == len(s):
                    ipAddr = ".".join(str(seg) for seg in segment)
                    ans.append(ipAddr)
                return
            if segStart == len(s):
                return
            if s[segStart] == "0":
                segment[segId] = 0
                dfs(segId + 1, segStart + 1)
            addr = 0
            for segEnd in range(segStart,len(s)):
                addr = 10*addr + ord(s[segEnd])-ord('0')
                if 0< addr <= 255:
                    segment[segId] = addr
                    dfs(segId+1,segEnd+1)
                else: break

        dfs(0,0)
        return ans
