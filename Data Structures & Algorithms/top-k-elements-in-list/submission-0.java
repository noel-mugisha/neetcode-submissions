class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();
        
        for (int num : nums) 
            map.put(num, map.getOrDefault(num, 0) + 1);
        
        List<Map.Entry<Integer, Integer>> entryList = new ArrayList<>(map.entrySet());
        // sort
        entryList.sort((a, b) -> Integer.compare(a.getValue(), b.getValue()));
        
        int[] result = new int[k];
        
        int i = 0, j = entryList.size() - 1;
        
        while (i < result.length) {
            result[i] = entryList.get(j).getKey();
            i++;
            j--;
        }
        
        return result;
    }
}
