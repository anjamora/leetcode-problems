class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1]*len(nums)

        tmp = 1
        for i in range(len(nums)):
            ans[i] = tmp
            tmp *= nums[i]
        tmp = 1
        for i in range(len(nums)-1,-1,-1):
            ans[i]*=tmp
            tmp *= nums[i]
        return ans
            