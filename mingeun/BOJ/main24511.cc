#include <cstdlib>
#include <iostream>
#include <deque>
#include <sstream>
using namespace std;

int main() {
    cin.tie(NULL);
    cout.tie(NULL);
    ios::sync_with_stdio(false);
    ostringstream oss;

    int n, m, x;
    cin >> n;
    deque<int> q;
    bool* isQueue = new bool[n];
    for (int i = 0; i < n; i++) {
        cin >> x;
        isQueue[i] = (x == 0);
    }
    for (int i = 0; i < n; i++) {
        cin >> x;
        if(isQueue[i]) {
            q.push_back(x);
        }
    }
    cin >> m;
    for (int i = 0; i < m; i++) {
        cin >> x;
        q.push_front(x);
    }
    for (int i = 0; i < m; i++) {
        oss << q.back() << " ";
        q.pop_back();
    }
    cout << oss.str() << endl;

    return 0;
}

