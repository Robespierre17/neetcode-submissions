class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}
        for index, number in enumerate(nums):
            partner = target - number
            if partner in seen: 
                return [seen[partner],index]
            seen[number] = index