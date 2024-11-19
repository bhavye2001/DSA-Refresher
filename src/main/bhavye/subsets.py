class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        index = 0
        output = []
        def rec_fn(index, output):
            # Base Case
            if index >= len(nums):
                ans.append(output)
                return;

            # Exclude
            rec_fn(index+1, output)

            # Include 
            element = nums[index]
            output.append(element)
            rec_fn(index+1, output)

        rec_fn(0, [])
        return ans
        