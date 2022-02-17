class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        vis = [False]*26
        nums = [0]*26
        stack = []
        for ch in s:
            nums[ord(ch) - ord('a')]+=1
        for i in range(len(s)):
            ch = s[i]
            idx = ord(ch) - ord('a')
            if not vis[idx]:
                while stack and ord(stack[-1])>ord(ch):
                    eidx = ord(stack[-1])
                    if nums[eidx] > 0:
                        stack.pop()
                        vis[eidx] = False
                    else:
                        break
                stack.append(ch)
                vis[idx] = True
        return ''.join(stack)