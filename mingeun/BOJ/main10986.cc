#include <vector>
#include <iostream>
#include <string>
using namespace std;

int main() {
    ios_base::sync_with_stdio(0);
	cin.tie(0);

    int n, m, x;
    long long sum = 0;
    cin >> n >> m;
    vector<long long> mcount(m, 0);
    long long answer = 0;
    for (int i = 0; i < n; i++) {
        cin >> x;
        sum += x;
        mcount[sum % m]++;
        if (sum % m == 0) answer++;
    }
    for (int i = 0; i < m; i++) {
        if (mcount[i] < 2) continue;
        answer +=mcount[i] * (mcount[i] - 1) / 2;
    }
    cout << answer << endl;
    return 0;
}


