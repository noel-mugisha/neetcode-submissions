class Solution {
    public boolean canJump(int[] nums) {
        int farthest = 0, i = 0;
        while (i < nums.length) {
            if (i > farthest)
                return false;
            farthest = Math.max(farthest, i + nums[i]);
            if (farthest >= nums.length-1)
                break;

            i++;
        }
        return true;
    }
}