class Solution {
    public boolean hasDuplicate(int[] nums) {
        // We create a set to keep track of the numbers we've encountered
        HashSet<Integer> seen = new HashSet<>();
        
        for (int num : nums) {
            // .contains() checks if the number is already in our set in O(1) time
            if (seen.contains(num)) {
                return true;
            }
            // If not, we add it to the set
            seen.add(num);
        }
        
        return false;
    }
}