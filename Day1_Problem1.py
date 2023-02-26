class Solution(object):
    def runningSum(self, nums):
        n =  len(nums)
        if n == 0:
            return[]
        running_sum = [nums[0]]
        for i in range(1,n):
            running_sum.append(running_sum[i-1]+nums[i])
        return (running_sum)
