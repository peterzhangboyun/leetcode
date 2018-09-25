class Solution(object):
    def searchInsert(self,num,target):
        for i in range(len(num)):
            if target == num[i]:
                return i

        for j in range(len(num)):
            if target <= num[j]:
                return j
        if target>num[len(num)-1]:
            return len(num)


a=Solution.searchInsert(Solution,[1,3,4,5],0)
print(a)