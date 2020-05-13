class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        tem_nums = nums[n-k%n:]+ nums[:n-k%n]
        for i in range(n):
            nums[i] = tem_nums[i]