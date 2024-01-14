#include <vector>
#include <iostream>
#include <cmath>
#include <numeric>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<vector<int>> dp(n + 1, vector<int>(10, 0));
    for (int i = 1; i <= 9; i++) dp[1][i] = 1;
    for (int i = 2; i <= n; i++) {
        for (int j = 0; j <= 9; j++) {
            if (j == 0) dp[i][j] = (dp[i - 1][1]) % 1000000000;
            else if (j == 9) dp[i][j] = (dp[i - 1][8]) % 1000000000;
            else dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j + 1]) % 1000000000;
        }
    }
    int answer = 0;
    for (int i = 0; i < 10; i++)
        answer = (answer + dp[n][i]) % 1000000000;
    cout << answer << endl;
    return 0;
}

