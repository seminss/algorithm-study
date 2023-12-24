#include <cstdlib>
#include <iostream>
#include <vector>
using namespace std;

const int N = 9;

bool okayToInsert(const vector<vector<int>>& sudoku, int x, int y, int v) {
    for (int i = 0; i < N; i++) {
        if (sudoku[x][i] == v)
            return false;
        if (sudoku[i][y] == v)
            return false;
    }
    int sqx = x / 3 * 3;
    int sqy = y / 3 * 3;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            if (sudoku[sqx + i][sqy + j] == v)
                return false;
        }
    }
    return true;
}

void dfs(vector<vector<int>>& sudoku, const vector<vector<int>>& emptySpaces, int d, bool& hit) {
    if (hit) {
        return;
    }
    if (d == emptySpaces.size()) {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++){
                cout << sudoku[i][j] << " ";
            }
            cout << endl;
        }
        hit = true;
        return;
    }
    for (int i = 1; i <= N; i++) {
        int x = emptySpaces[d][0];
        int y = emptySpaces[d][1];
        if (okayToInsert(sudoku, x, y, i)) {
            sudoku[x][y] = i;
            dfs(sudoku, emptySpaces, d + 1, hit);
            sudoku[x][y] = 0;
        }
    }
}

int main() {
    cin.tie(NULL);
    cout.tie(NULL);
    ios::sync_with_stdio(false);

    vector<vector<int>> emptySpaces;
    vector<vector<int>> sudoku(N, vector<int>(N, 0));
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cin >> sudoku[i][j];
            if (sudoku[i][j] == 0)
                emptySpaces.push_back(vector<int>{i, j});
        }
    }
    bool hit = false;
    dfs(sudoku, emptySpaces, 0, hit);

    return 0;
}
