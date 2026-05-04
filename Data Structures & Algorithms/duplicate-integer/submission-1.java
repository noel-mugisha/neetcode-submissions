class Solution {
    public boolean hasDuplicate(int[] nums) {
        Arrays.sort(nums);
        if (nums.length <= 1) return false;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] == nums[i-1]) return true;
        }
        return false;
    }
}