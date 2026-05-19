class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        seen = set()
        for num in nums:
            if num in seen:
                return True
            else: 
                seen.add(num)
        return False
        

        seen = set()
        for x in nums:
            if x in seen:
                return True
            else:
                seen.add(x)
        return False





        # does a number in the list equal a number already in the list?
        # if so, return true
        # if not, return false
        # SO, check the whole list to the see if any number equals any other number in the list