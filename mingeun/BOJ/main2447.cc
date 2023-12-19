#include <iostream>
#include <vector>
using namespace std;

void recursive(int x1, int x2, int y1, int y2, int i, int j, vector<vector<char>>& pattern) {
    int l = x2 - x1;
    if (i == 1 && j == 1) {
        for (int i = x1; i < x2; i++) {
            for (int j = y1; j < y2; j++) {
                pattern[i][j] = ' ';
            }
        }
        return;
    }
    if (l == 1) {
        return;
    }
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            int xn1 = x1 + i * l / 3;
            int xn2 = x1 + (i + 1) * l / 3;
            int yn1 = y1 + j * l / 3;
            int yn2 = y1 + (j + 1) * l / 3;
            recursive(xn1, xn2, yn1, yn2, i, j, pattern);
        }
    }
}

int main() {
    cin.tie(NULL);
    cout.tie(NULL);
    ios::sync_with_stdio(false);

    int n;
    cin >> n;
    vector<vector<char>> pattern(n, vector<char>(n, '*'));
    recursive(0, n, 0, n, 0, 0, pattern);

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cout << pattern[i][j];
        }
        cout << "\n";
    }

    return 0;
}
