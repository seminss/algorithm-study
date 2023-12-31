#include <vector>
#include <iostream>
using namespace std;

int main() {
    int T;
    cin >> T;

    const int N = 100;
    vector<long long> dp(N + 1, 1);
    dp[4] = 2; dp[5] = 2;
    int j = 1;
    for (int i = 6; i <= N; i++) {
        dp[i] = dp[i - 1] + dp[j++];
    }
    for (int i = 0; i < T; i++) {
        int n;
        cin >> n;
        cout << dp[n] << endl;
    }
    return 0;
}

