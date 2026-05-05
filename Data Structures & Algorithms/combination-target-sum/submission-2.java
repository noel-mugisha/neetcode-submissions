class Solution {
    public List<List<Integer>> combinationSum(int[] nums, int target) {
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
        if (remaining < 0) return;
        if (i == nums.length) return;

        current.add(nums[i]);
        backtrack (nums, remaining-nums[i], i, current, combinations);

        current.remove(current.size() - 1);
        backtrack (nums, remaining, i+1, current, combinations);
    }
}