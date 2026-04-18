class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = {}
        for i in range(len(nums)):
            c = target - nums[i]
            if c in n:
                return [n[c],i]
            n[nums[i]] = i

