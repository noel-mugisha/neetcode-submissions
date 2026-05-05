class Solution {
    public List<List<Integer>> combinationSum(int[] nums, int target) {
        Arrays.sort(nums);
        List<List<Integer>> combinations = new ArrayList<>();
        List<Integer> current = new ArrayList<>();
        backtrack(nums, target, 0, current, combinations);
        return combinations;
    }

    void backtrack(int[] nums, int remaining, int i, List<Integer> current, List<List<Integer>> combinations) {
        if (remaining == 0) {
            combinations.add(new ArrayList<>(current));
            return;
        }
        if (i == nums.length) return;
        if (nums[i] > remaining) return;

        current.add(nums[i]);
        backtrack (nums, remaining-nums[i], i, current, combinations);

        current.remove(current.size() - 1);
        backtrack (nums, remaining, i+1, current, combinations);
    }
}