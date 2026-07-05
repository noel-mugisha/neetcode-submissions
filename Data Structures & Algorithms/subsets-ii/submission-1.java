class Solution {
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> subs = new ArrayList<>();
        List<Integer> curr = new ArrayList<>();

        dfs(nums, 0, curr, subs);

        return subs;
    }

    void dfs (int[] nums, int i, List<Integer> curr, List<List<Integer>> subs) {
        if (i == nums.length) {
            subs.add(new ArrayList<>(curr));
            return;
        }

        curr.add(nums[i]);
        dfs(nums, i + 1, curr, subs);
        curr.removeLast();


        int j = i + 1;
        while (j < nums.length && nums[j] == nums[i])
            j++;

        dfs(nums, j, curr, subs);
    }
}
