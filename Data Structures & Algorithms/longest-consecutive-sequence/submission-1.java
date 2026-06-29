class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> set = new HashSet<>();
        int longest = 0;
        for (int num : nums)
            set.add(num);

        for (int num : set) {
            if (!set.contains(num - 1)) {
                int len = 0;
                while (set.contains(num + len))
                    len++;
                longest = Math.max(longest, len);
            }
        }
        return longest;
    }
}
