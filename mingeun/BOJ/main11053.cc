#include <vector>
#include <iostream>
#include <cmath>
using namespace std;

int main() {

    int n;
    cin >> n;
    vector<int> numbers(n, 0);
    for (int i = 0; i < n; i++) {
        cin >> numbers[i];
    }
    vector<int> dp(n, 1);
    int answer = dp[0];
    for (int i = 1; i < n; i++) {
        for (int j = 0; j < i; j++) {
            if (numbers[i] > numbers[j]) {
                dp[i] = max(dp[j] + 1, dp[i]);
            }
        }
        answer = max(answer, dp[i]);
    }
    cout << answer << endl;
    return 0;
}

