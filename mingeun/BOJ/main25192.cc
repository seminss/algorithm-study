#include <iostream>
#include <string>
#include <unordered_set>
using namespace std;

int main() {
    cin.tie(NULL);
    cout.tie(NULL);
    ios::sync_with_stdio(false);

    int n;
    int answer = 0;
    string msg;
    cin >> n;
    unordered_set<string> memberUsedEmoticon;
    for (int i = 0; i < n; i++) {
        cin >> msg;
        if (msg == "ENTER") {
            memberUsedEmoticon = unordered_set<string>();
            continue;
        }
        if (memberUsedEmoticon.find(msg) != memberUsedEmoticon.end()) {
            continue;
        }
        if (memberUsedEmoticon.find(msg) == memberUsedEmoticon.end()) {
            memberUsedEmoticon.insert(msg);
            answer++;
            continue;
        }
    }
    cout << answer << endl;

    return 0;
}

