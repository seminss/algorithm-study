#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int n;
    cin >> n;
    int** triangle = new int*[n];
    for (int i = 0; i < n; i++) {
        triangle[i] = new int[i + 1];
        for (int j = 0; j < i + 1; j++) {
            cin >> triangle[i][j];
        }
    }
    for (int i = 1; i < n; i++) {
        for (int j = 0; j < i + 1; j++) {
            if (j == 0) {
                triangle[i][j] = triangle[i - 1][j] + triangle[i][j];
                continue;
            }
            if (j == i) {
                triangle[i][j] = triangle[i - 1][j - 1] + triangle[i][j];
                continue;
            }
            triangle[i][j] = max(triangle[i - 1][j], triangle[i - 1][j - 1]) + triangle[i][j];
        }
    }
    int answer = 0;
    for (int i = 0; i < n; i++) {
        answer = max(triangle[n - 1][i], answer);
    }
    cout << answer << endl;
    return 0;
}
