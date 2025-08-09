



class Solution(object):
    def twoSum(self, nums, target):
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1,n):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return []

test_cases = [
    ([2, 7, 11, 15], 9),    # Expected output: [0, 1]
    ([3, 2, 4], 6),         # Expected output: [1, 2]
    ([3, 3], 6),            # Expected output: [0, 1]
    ([1, 2, 3, 4, 5], 10),  # Expected output: []
]

sol = Solution()

for i, (nums, target) in enumerate(test_cases, 1):
    result = sol.twoSum(nums, target)
    print(f"Test case {i}: nums = {nums}, target = {target} => result = {result}")