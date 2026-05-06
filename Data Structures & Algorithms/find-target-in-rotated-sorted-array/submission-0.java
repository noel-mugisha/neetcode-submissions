class Solution {
    public int search(int[] nums, int target) {
        int pivot = findPivot(nums);
        int ls = binarySearch(nums, target, 0, pivot-1);
        if (ls != -1) return ls;
        return binarySearch(nums, target, pivot, nums.length-1);
    }
    
    int findPivot (int[] nums) {
        int s = 0;
        int e = nums.length-1;
        while (s < e) {
            int mid = s + (e - s)/2;
            if (nums[mid] <= nums[e])
                e = mid;
            else 
                s = mid + 1;
        }
        return s;
    }
    
    int binarySearch (int[] nums, int target, int s, int e) {
        while (s <= e) {
            int mid = s + (e - s)/2;
            if (nums[mid] == target)
                return mid;
            if (nums[mid] < target)
                s = mid + 1;
            else 
                e = mid - 1;
        }
        
        return -1;
    }
}
 