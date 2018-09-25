class Solution(object):
    def countAndSay(self, n):
        if n==1:
            return "1"
        x='1'
        for i in range(n-1):
            before,y,count=x[0],'',0
            for j in x:
                if before==j:
                    count=count+1
                else:
                    y=y+str(count)+before
                    before=j
                    count=1
            y=y+str(count)+before
            x=y
        return x
z=Solution.countAndSay(Solution,2)
print(z)

