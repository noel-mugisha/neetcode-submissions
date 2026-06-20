class Solution {
    public List<List<String>> solveNQueens(int n) {
        char[][] board = new char[n][n];
        for (char[] arr : board)
            Arrays.fill(arr, '.');
        
        List<List<String>> res = new ArrayList<>();
        
        backtrack(board, n, 0, 0, res);
        
        return res;
    }

    void backtrack(char[][] board, int remaining, int row, int col, List<List<String>> res) {
        if (remaining == 0) {
            List<String> curr = new ArrayList<>();
            for (char [] arr : board)
                curr.add(new String(arr));
            res.add(curr);
        }

        if (col == board.length) {
            return;
        }

        if (row == board.length)
            return;


        if (isSafe(board, row, col)) {
            board[row][col] = 'Q';
            backtrack(board, remaining - 1, row + 1, 0, res);
            board[row][col] = '.';
        }

        backtrack(board, remaining, row, col + 1, res);
    }

    boolean isSafe(char[][] board, int row, int col) {
        int n = board.length;

        // check upward
        for (int r = row; r >= 0; r--) {
            if (board[r][col] == 'Q')
                return false;
        }

        // check rD
        for (int r = row, c = col; r >= 0 && c < n ; r--, c++) {
            if (board[r][c] == 'Q')
                return false;
        }

        // check lD
        for (int r = row, c = col; r >= 0 && c >= 0; r--, c--) {
            if (board[r][c] == 'Q')
                return false;
        }

        return true;
    }
}
