class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
            count = Counter(nums)
            mais_freq = count.most_common(k)
            return [num for num,freq in mais_freq]
