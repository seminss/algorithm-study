#include <vector>
#include <iostream>
#include <string>
#include <cmath>
using namespace std;

int minCountForGivenStartColor(const vector<vector<char>>& board, char color, int k) {
    int n = board.size();
    int m = board[0].size();
    vector<vector<int>> psum(n, vector<int>(m, 0));
    char ecolor = color;
    char ocolor = (ecolor == 'B') ? 'W' : 'B';
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if ((i + j) % 2 == 0 && board[i][j] != ecolor) psum[i][j] = 1;
            if ((i + j) % 2 == 1 && board[i][j] != ocolor) psum[i][j] = 1;
        }
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (i == 0 && j == 0) continue;
            if (i == 0) psum[i][j] += psum[i][j - 1];
            else if (j == 0) psum[i][j] += psum[i - 1][j];
            else psum[i][j] += psum[i - 1][j] + psum[i][j - 1] - psum[i - 1][j - 1];
        }
    }
    int count = 999999999;
    for (int i = 0; i <= n - k; i++) {
        for (int j = 0; j <= m - k; j++ ) {
            if (i == 0 && j == 0)
                count = min(count, psum[i + k - 1][j + k - 1]);
            else if (i == 0) count = min(count, psum[i + k -1][j + k - 1] - psum[i + k - 1][j - 1]);
            else if (j == 0) count = min(count, psum[i + k -1][j + k - 1] - psum[i - 1][j + k - 1]);
            else {
                count = min(count, psum[i + k - 1][j + k - 1] 
                        - psum[i + k - 1][j - 1] - psum[i - 1][j + k - 1]
                        + psum[i - 1][j - 1]);
            }
        }
    }
    return count;
}

int main() {
    const char BLACK = 'B';
    const char WHITE = 'W';
    int n, m, k;
    cin >> n >> m >> k;
    vector<vector<char>> board(n, vector<char>(m, 0));
    char x;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> x;
            board[i][j] = x;
        }
    }
    int answer = minCountForGivenStartColor(board, BLACK, k);
    answer = min(answer, minCountForGivenStartColor(board, WHITE, k));
    cout << answer << endl;
    return 0;
}

