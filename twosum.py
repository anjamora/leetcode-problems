class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pos1 = 0
        pos2 = 1
        for i in nums:
            for j in range(pos2, len(nums)):
                if i + nums[j] == target:
                    return pos1, j
            pos2 += 1
            pos1 += 1
