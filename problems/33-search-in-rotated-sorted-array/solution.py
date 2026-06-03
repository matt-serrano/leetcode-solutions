        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid

            # left sorted portion
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1     
            # right sorted portion               
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
    def search(self, nums: List[int], target: int) -> int:
class Solution:
        l, r = 0, len(nums) - 1

