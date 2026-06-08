class Solution {
    public int maxArea(int[] heights) {
        int maxArea = Integer.MIN_VALUE;
        int i = 0, j = heights.length - 1;
        while (i < j) {
            int width = j - i;
            int length = Math.min(heights[i], heights[j]);
            maxArea = Math.max(maxArea, length * width);

            if (heights[i] < heights[j]) {
                i++;
            } else {
                j--;
            }
        }

        return maxArea;
    }
}
