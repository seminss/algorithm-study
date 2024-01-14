#include <vector>
#include <iostream>
#include <cmath>
using namespace std;

const int R = 0;
const int G = 1;
const int B = 2;
int main() {
    int n;
    cin >> n;
    vector<vector<int>> costs(n, vector<int>(3, 0));
    for (int i = 0; i < n; i++) {
        cin >> costs[i][R];
        cin >> costs[i][G];
        cin >> costs[i][B];
    }
    vector<vector<int>> dp(3, vector<int>(n, 0));
    dp[R][0] = costs[0][R];
    dp[G][0] = costs[0][G];
    dp[B][0] = costs[0][B];
    for (int i = 1; i < n; i++) {
        dp[R][i] = min(dp[G][i - 1], dp[B][i - 1]) + costs[i][R];  // B, G
        dp[G][i] = min(dp[R][i - 1], dp[B][i - 1]) + costs[i][G];  // R, B
        dp[B][i] = min(dp[R][i - 1], dp[G][i - 1]) + costs[i][B];  // R, G
    }
    cout << min(dp[R][n - 1], min(dp[G][n - 1], dp[B][n - 1])) << endl;
}

