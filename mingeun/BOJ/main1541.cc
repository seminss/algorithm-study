#include <vector>
#include <iostream>
#include <string>
using namespace std;

bool isDigit(char c) {
    return (c <= '9' && c >= '0');
}

int main() {
    string exp, tmp;
    cin >> exp;
    int answer = 0;
    int coefficient = 1;
    for (int i = 0; i < exp.length(); i++) {
        if (isDigit(exp[i])) {
            tmp.push_back(exp[i]);
            if (i == exp.length() - 1) {
                answer += coefficient * stoi(tmp);
            }
            continue;
        }
        answer += coefficient * stoi(tmp);
        if (exp[i] == '-') {
            coefficient = -1;
        }
        tmp = "";
    }
    cout << answer << endl;
    return 0;
}
