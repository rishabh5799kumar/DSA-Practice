class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        product = 1
        arr = [1] * n

        for i in range(n):
            arr[i] = product
            product *= nums[i]

        product = 1
        for i in range(n-1, -1, -1):
            arr[i] *= product 
            product *= nums[i]
        
        return arr