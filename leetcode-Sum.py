class Solution(object):
    def twoSum(self, nums, target):
        dict={}
        for i in  range(len(nums)):
            if  target-nums[i] in dict:#  target-nums[i]为key
                return  [dict[target-nums[i]],i]
            dict[nums[i]]=i
        return  []

myinput=Solution.twoSum(Solution,[1, 3, 5, 2, 4], 6)
print (myinput)
