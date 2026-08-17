class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()

        for i in range(len(nums) + 1):
            if i >= k:
                res.append(nums[q[0]])
                if i == len(nums):
                    break
                
                if q[0] == i - k:
                    q.popleft()
            
            while q and nums[i] > nums[q[-1]]:
                q.pop()
            
            q.append(i)

        return res
        