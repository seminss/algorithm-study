#include <iostream>
#include <string>
#include <stack>
#include <queue>
using namespace std;

string simulate(queue<int>& _queue) {
    int next = 1;
    stack<int> _stack;
    while (!_queue.empty() || !_stack.empty()) {
        if ((!_queue.empty() && _queue.front() != next && !_stack.empty() && _stack.top() != next) ||
            (_queue.empty() && _stack.top() != next)) {
            return "Sad\n";
        }
        if (!_queue.empty() && _queue.front() == next) {
            _queue.pop();
            next++;
        }
        while (!_stack.empty() && _stack.top() == next) {
            _stack.pop();
            next++;
        }
        while (!_queue.empty() && _queue.front() != next) {
            _stack.push(_queue.front());
            _queue.pop();
        }
    }
    return "Nice\n";
}

int main() {
    cin.tie(NULL);
    cout.tie(NULL);
    ios::sync_with_stdio(false);

    int n;
    cin >> n;
    queue<int> _queue;
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        _queue.push(x);
    }
    cout << simulate(_queue);

    return 0;
}


