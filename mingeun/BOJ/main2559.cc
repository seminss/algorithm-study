#include <vector>
#include <iostream>
#include <string>
#include <queue>
using namespace std;

int main() {
    int n, k;
    cin >> n >> k;
    int answer = -2000000000;
    queue<int> q;
    int psum = 0;
    int s = 0;
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        psum += x;
        q.push(x);
        if (i == k - 1) {
            answer = psum;
            continue;
        }
        if (i >= k) {
            s = q.front();
            q.pop();
            psum -= s;
            answer = max(answer, psum);
        }
    }
    cout << answer << endl;
    return 0;
}
