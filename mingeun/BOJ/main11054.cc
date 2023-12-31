#include <vector>
#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> A(n, 0);
    for (int i = 0; i < n; i++) {
        cin >> A[i];
    }

    // left to right
    vector<int> dp1(n, 1);
    for (int i =1; i < n; i++) {
        for (int j = 0; j < i; j++) {
            if (A[j] < A[i]) dp1[i] = max(dp1[i], dp1[j] + 1);
        }
    }
    // right to left
    vector<int> dp2(n, 1);
    for (int i = n - 2; i > -1 ; i--) {
        for (int j = n - 1; j > i; j--) {
            if (A[j] < A[i]) dp2[i] = max(dp2[i], dp2[j] + 1);
        }
    }

    int answer = 0;
    for (int i = 0; i < n; i++) {
        answer = max(answer, dp1[i] + dp2[i]);
    }
    cout << answer - 1 << endl;
    return 0;
}

