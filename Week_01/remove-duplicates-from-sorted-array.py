class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return;
        tem_index = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[tem_index] = nums[i]
                tem_index += 1
        return tem_index