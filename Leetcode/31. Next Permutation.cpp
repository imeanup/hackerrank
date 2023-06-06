class Solution {
public:

    void nextPermutation(vector<int>& nums) {
        int i = nums.size() - 2;
        while (i >= 0 && nums[i+1] <= nums[i]){
            i--;
        }
        if (i >= 0){
            int j = nums.size() - 1;
            while (nums[j] <= nums[i]){
                j--;
            }
            swap(nums[i], nums[j]);
        }
        reverse(nums.begin() + (i+1), nums.end());
    }
};

/*
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # permutation = n!

        i = len(nums) - 2
        while i >= 0 and nums[i+1] <= nums[i]:
                i -= 1

        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        nums[i+1:] = nums[i+1:][::-1]
*/
