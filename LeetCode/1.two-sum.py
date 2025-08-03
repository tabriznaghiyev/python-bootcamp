class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash_map = {}
        for i, v in enumerate(nums):
            complement = target - v
            if complement in hash_map:
                return [hash_map[complement], i]
            hash_map[v] = i
        return []