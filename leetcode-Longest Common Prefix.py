class Solution(object):
    def common(self,s):
        if not s:
            return''
        res=''
        for j in range(len(s[0])):
            for i in range(1,len(s)):
                if s[i][j] != s[0][j]:
                    return res
            res = res + s[0][j]
        return res
a=Solution.common(Solution,['hahafec','hahah','hahagggg'])
print(a)