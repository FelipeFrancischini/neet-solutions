class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for number in range(len(nums)):
            for prox_number in range(number + 1, len(nums)):
                if nums[number] + nums[prox_number] == target:
                    return [number, prox_number]
        return []
