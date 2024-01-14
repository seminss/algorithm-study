#include <iostream>
#include <sstream>
using namespace std;

void movePlates(int p, int ss, int se, int tmp, int& answer, ostringstream& oss) {
    if (p == 1) {
        oss << ss << " " << se << "\n";
        answer++;
        return;
    }
    movePlates(p - 1, ss, tmp, se, answer, oss);
    movePlates(1, ss, se, tmp, answer, oss);
    movePlates(p - 1, tmp, se, ss, answer, oss);
}

int main() {
    cin.tie(NULL);
    cout.tie(NULL);
    ios::sync_with_stdio(false);

    int n;
    cin >> n;
    int answer = 0;
    ostringstream oss;
    movePlates(n, 1, 3, 2, answer, oss);
    cout << answer << endl << oss.str();

    return 0;
}

