// 23.12.8 23:24 ~ 11:30
#include <iostream>
#include <stack>
using namespace std;
int main() {
    cout.tie(NULL);
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    int k, n;
    int sum = 0;
    stack<int> numbers;
    cin >> k;
    for (int i = 0; i < k; i++) {
        cin >> n;
        if (n == 0) {
            numbers.pop();
            continue;
        }
        numbers.push(n);
    }
    while (!numbers.empty()) {
        sum += numbers.top();
        numbers.pop();
    }
    cout << sum << endl;
}
