#include <vector>
#include <iostream>
#include <cmath>
#include <string>
using namespace std;

int main() {
    const int W = 0;
    const int V = 1;
    int N, K;
    cin >> N >> K;
    vector<vector<int>> items(N + 1, vector<int>(2, 0));
    for (int i = 1; i <= N; i++) {
        cin >> items[i][W] >> items[i][V];
    }
    vector<vector<int>> dp(N + 1, vector<int>(K + 1, 0));
    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= K; j++) {
            if (items[i][W] <= j) {
                dp[i][j] = dp[i - 1][j - items[i][W]] + items[i][V];
            } else {
                dp[i][j] = dp[i][j - 1];
            }
            dp[i][j] = max(dp[i][j], dp[i - 1][j]);
        }
    }
    cout << dp[N][K] << endl;
    return 0;
}
