class Solution:
    def firstUniqChar(self, s):
        unique = {}
        boo = -1
        count =0
        for c in s:
            if c not in unique:
                unique[c] = 1
            else:
                unique[c] +=1
        for i in range(len(s)):
            if unique[s[i]] == 1:
                boo = i
                break
        return boo
print(Solution().firstUniqChar("ababbdp"))