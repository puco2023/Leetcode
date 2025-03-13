class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        window=set()
        for i in range(len(nums)):
            if nums[i] in window:
                return True
            window.add(nums[i])
            if k<=i:
                window.remove(nums[i-k])
        return False
