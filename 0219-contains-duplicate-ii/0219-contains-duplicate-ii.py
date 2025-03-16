class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        visited = set()

        for i, val in enumerate(nums):
            if val in visited:
                return True
            
            visited.add(val)

            if len(visited) > k:
                visited.remove(nums[i-k])
        
        return False
            