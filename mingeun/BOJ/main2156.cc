#include <vector>
#include <iostream>
#include <cmath>
#include <numeric>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> glasses(n, 0);
    for (int i = 0; i < n; i++) {
        cin >> glasses[i];
    }
    if (n < 3) {
        cout <<  accumulate(glasses.begin(), glasses.end(), 0) << endl;
        return 0;
    }
    vector<int> dp(n, 0);
    dp[0] = glasses[0];
    dp[1] = glasses[0] + glasses[1];
    dp[2] = max(dp[1], max(glasses[1], glasses[0]) + glasses[2]);
    for (int i = 3; i < n; i++) {
        dp[i] = max(dp[i - 2], dp[i - 3] + glasses[i - 1]) + glasses[i];
        dp[i] = max(dp[i], dp[i - 1]);
    }
    cout << dp[n - 1] << endl;
    return 0;
}
