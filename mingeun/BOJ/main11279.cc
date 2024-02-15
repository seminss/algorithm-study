#include <sstream>
#include <iostream>
#include <queue>
using namespace std;

int main() {
    int n, x;
    ostringstream oss;
    cin >> n;
    priority_queue<int> pq;
    for (int i{}; i < n; i++) {
        cin >> x;
        if (x == 0) {
            if (pq.empty()) {
                oss << "0" << endl;
            } else {
                oss << pq.top() << endl;
                pq.pop();
            }
        } else {
            pq.push(x);
        }
    }
    cout << oss.str();
    return 0;
}
