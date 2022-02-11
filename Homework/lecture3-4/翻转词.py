class Solution:
    def reverseWords(self, s: str) -> str:
        if not s:
            return s
        s_list = s.split(' ')
        res = [0]*len(s_list)
        for i in range(len(s_list)):
            res[-1-i] = s_list[i]
        res = [x.strip() for x in res if x != '']
        return ' '.join(res)  