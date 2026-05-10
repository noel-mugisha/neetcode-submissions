class Solution {
    public int uniquePaths(int m, int n) {
        int r = 0, c= 0;
        Integer[][] dp = new Integer[m][n];
        return helper (r, c, m, n, dp);
    }

    int helper (int r, int c, int m, int n, Integer[][] dp) {
        if (r == m-1 || c == n-1)
            return 1;
        if (dp[r][c] != null) 
            return dp[r][c];

        int right = helper (r, c+1, m, n, dp);
        int down = helper (r+1, c, m, n, dp);

        return dp[r][c] = right + down;
    }
}
