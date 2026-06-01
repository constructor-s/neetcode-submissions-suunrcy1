class Solution {
public:
    vector<vector<string>> solveNQueens(int n) {
        std::vector<std::vector<std::string>> res;

        // Each row can only have one queen
        // Others need to be marked more explicitly
        std::vector<bool> cols(n, false);
        std::vector<bool> diag1(n * 2, false); // x + y == constant
        std::vector<bool> diag2(n * 2, false); // x - y == constant

        std::vector<std::string> board(n, std::string(n, '.'));

        backtrack(0, res, n, board, cols, diag1, diag2);

        return res;
    }
private:
    void backtrack(const int i, std::vector<std::vector<std::string>> & res, 
                    int n, std::vector<std::string> & board,  
                    std::vector<bool> & cols, std::vector<bool> & diag1, std::vector<bool> & diag2) {
        if (i == n) {
            res.push_back(board);
            return;
        }

        for (int j = 0; j < n; ++j) {
            if ((!cols[j]) && 
                (!diag1[i + j]) &&
                (!diag2[n + i - j])) {
                cols[j] = true;
                diag1[i + j] = true;
                diag2[n + i - j] = true;

                board[i][j] = 'Q';
                backtrack(i + 1, res, n, board, cols, diag1, diag2);
                board[i][j] = '.';

                
                cols[j] = false;
                diag1[i + j] = false;
                diag2[n + i - j] = false;
            }
        }
    }
};
