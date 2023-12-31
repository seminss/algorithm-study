#include <vector>
#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> l(501, 0);
    vector<int> dp(501, 1);
    for (int i = 0; i < n; i++) {
        int a, b;
        cin >> a >> b;
        l[a] = b;
    }
    int m = 0;
    for (int i = 1; i <= 500; i++) {
        if (l[i] == 0) continue;
        for (int j = 1; j < i; j++) {
            if (l[j] == 0) continue;
            if (l[i] > l[j]) dp[i] = max(dp[j] + 1, dp[i]);
        }
        m = max(m, dp[i]);
    }
    cout << n - m << endl;
    return 0;
}
