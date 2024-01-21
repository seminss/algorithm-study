#include <vector>
#include <iostream>
#include <string>
#include <sstream>
#include <cmath>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    vector<vector<int>> psumy(n, vector<int>(n, 0));
    for (int i = 0; i < n; i++) {
        int tmp = 0;
        int x;
        for (int j = 0; j < n; j++) {
            cin >> x;
            tmp += x;
            psumy[i][j] = tmp;
        }
    }
    ostringstream oss;
    int tmp = 0;
    // O(N * M) <= 10^8
    for (int i = 0; i < m; i++) {
        int answer = 0;
        int x1, x2, y1 , y2;
        int a, b, c, d;
        cin >> a >> b >> c >> d;
        x1 = min(a, c) - 1;
        x2 = max(a, c) - 1;
        y1 = min(b, d) - 1;
        y2 = max(b, d) - 1;
        for (int i = x1; i <= x2; i++) {
            if (y1 == 0) answer += psumy[i][y2];
            else answer += psumy[i][y2] - psumy[i][y1 - 1];
        }
        oss << answer << endl;
    }
    cout << oss.str();
    return 0;
}

