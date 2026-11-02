class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map_ = Counter(nums)
        n = len(nums)
        bucket = [[] for _ in range(n + 1)]

        for key, value in map_.items():
            bucket[value].append(key)
        
        res = []
        for i in range(n, -1, -1):
            for el in bucket[i]:
                res.append(el)
                k -= 1
                if k == 0:
                    return res
        