import sys

class Solution(object):
    def mergeTwoLists(self, a):
        if len(a) == 0:
            return 0
        j = 0

        for i in range(0, len(a)):
            if a[j] != a[i]:
                a[j+1] = a[i]
                j = j+1
        return j+1

b=Solution.mergeTwoLists(Solution , [1,1,1,2,2,3,4,5])
print(b)
