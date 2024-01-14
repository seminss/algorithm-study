#include <iostream>
#define NU first
#define DE second
using namespace std;

typedef pair<int, int> fraction;

int a, b;
fraction answer;
fraction fractions[2];

// a >= b
int gcd(int _a, int _b) {
    while (_b != 0) {
        int tmp = _b;
        _b = _a % _b;
        _a = tmp;
    }
    return _a;
}

int main() {
    cin.tie(NULL);
    ios::sync_with_stdio(false);
    for (int i = 0; i < 2; i++) {
        cin >> fractions[i].NU;
        cin >> fractions[i].DE;
    }
    answer.NU = fractions[0].NU * fractions[1].DE + fractions[1].NU * fractions[0].DE;
    answer.DE = fractions[0].DE * fractions[1].DE;
    int x = gcd(answer.NU, answer.DE);
    cout << answer.NU / x << endl << answer.DE / x << endl;
    return 0;
}

