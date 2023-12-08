// 23:42 ~ 23:53
#include <iostream>
#include <string>
#include <stack>
#include <sstream>
using namespace std;

const char OPEN = '(';
const char CLOSE = ')';
const string YES = "YES";
const string NO = "NO";

bool vps(string s) {
    stack<char> _stack;
    for (const char c : s) {
        if (c == OPEN) {
            _stack.push(OPEN);
        } else if (_stack.empty()) {
            return false;
        } else {
            _stack.pop();
        }
    }
    if (_stack.empty()) { 
        return true;
    }
    return false;
}

int main() {
    cin.tie(NULL);
    cout.tie(NULL);
    ios::sync_with_stdio(false);
    int T;
    cin >> T;
    ostringstream oss;
    for (int i = 0; i < T; i++) {
        string s;
        cin >> s;
        if (vps(s)) {
            oss << YES << endl;
        } else {
            oss << NO << endl;
        }
    }
    cout << oss.str();
    return 0;
}

