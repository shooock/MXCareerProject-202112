class Solution:
    #注意用len(s),不是(len(s_list))
    def reverseVowels(self, s: str) -> str:
        if not s:
            return s
        left = 0
        right = len(s)-1
        s_list = list(s)
        voewl = "aeiouAEIOU"
        while left < right:
            if s_list[left] in voewl and s_list[right] in voewl:
                s_list[left], s_list[right] = s_list[right], s_list[left]
                right -= 1
                left += 1
            if s_list[right] not in voewl:
                right -= 1
            if s_list[left] not in voewl:
                left += 1
        return ''.join(s_list)
