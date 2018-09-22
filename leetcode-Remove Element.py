class Solution:
                def remove(self, s, a):
                    b=len(s)+1
                    for i in range(len(s)):
                        if s[i]==a:
                            b=b-1
                            s[i]=s[i+1]
                            i=i-1
                    for j in range(b - 1):
                        print(s[j])
                    return (b-1)


tset=Solution.remove(Solution,[3,4,3,2,3,2,3],2)
print(tset)