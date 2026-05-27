class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        n = len(nums)
        seen = set()

        duplicate = -1
        total = 0

        for num in nums:
            if num in seen:
                duplicate = num
            seen.add(num)
            total += num

        expected = n * (n + 1) // 2
        missing = expected - (total - duplicate)

        return [duplicate, missing]
                
        