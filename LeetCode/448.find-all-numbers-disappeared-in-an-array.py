class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        set_nums = set(nums)
        ret = []
        for i in range(1,len(nums)+1):
            if i not in set_nums:
                ret.append(i)
        return ret

sol=Solution()
print(sol.findDisappearedNumbers([4,3,5,2,3,1,1,1]))