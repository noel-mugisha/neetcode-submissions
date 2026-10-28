class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        max_prod = float("-inf")
        prod = 1

        for i in range(n):
            prod *= nums[i]
            max_prod = max(max_prod, prod)

            if prod == 0:
                prod = 1
        
        prod = 1
        for i in range(n - 1, -1, -1):
            prod *= nums[i]
            max_prod = max(max_prod, prod)

            if prod == 0:
                prod = 1
        
        return max_prod