#include <cmath>
#include <iostream>
#include <vector>
using namespace std;

bool safeToAdd(const vector<int>& queens, int x, int y) {
    for (int i = 0; i < queens.size(); i++) {
        // 대각선 또는 행이 같은 경우
        if (abs(queens[i] - x) == abs(i - y) || x == queens[i]) {
            return false;
        }
    }
    return true;
}

void dfs(int n, vector<int>& queens, int& answer) {
    if (queens.size() == n) {
        answer++;
        return;
    }
    // i행 j열에 퀸 추가
    int j = queens.size();
    for (int i = 0; i < n; i++) {
        if (safeToAdd(queens, i, j)) {
            queens.push_back(i);
            dfs(n, queens, answer);
            queens.pop_back();
        }
    }
}


int main() {
    cin.tie(NULL);
    cout.tie(NULL);
    ios::sync_with_stdio(false);

    int n = 0, answer = 0;
    cin >> n;
    vector<int> queens;
    dfs(n, queens, answer);
    cout << answer << endl;

    return 0;
}

