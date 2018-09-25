class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x=0
        a=-2**31
        for i in range(len(nums)):
            if x<0:
                x=0
            x=x+nums[i]
            a=max(a,x)
        return a

b=Solution.maxSubArray(Solution,[1,-1,2,3,-1,-2,4,6])
print(b)