#include <bits/stdc++.h>
using namespace std;
int main() {
    int n;
    cin >> n;
    vector<int> inputs(n, 0);
    for (int i = 0; i < n; i++) {
        cin >> inputs[i];
    }
    vector<int> alignedX(inputs);
    unordered_map<int, int> map;
    sort(alignedX.begin(), alignedX.end());
    for (int i = 0; i < n; i++) {
        if (i == 0) {
            map[alignedX[i]] = 0;
            continue;
        }
        if (i > 0 && alignedX[i] == alignedX[i - 1]) {
            map[alignedX[i]] = map[alignedX[i - 1]];
            continue;
        }
        map[alignedX[i]] = map[alignedX[i - 1]] + 1;
    }
    ostringstream oss;
    for (int i = 0; i < n; i++) {
        oss << map[inputs[i]] << " ";
    }
    cout << oss.str() << endl;
    return 0;
}


