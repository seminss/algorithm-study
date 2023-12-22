#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

#define PLUS 0
#define MINUS 1
#define MULT 2
#define DIV 3

void permute(int n, vector<vector<int>>& results, const vector<int> operators, vector<int>& tmp, vector<bool>& u) {
    if (tmp.size() == n) {
        results.push_back(tmp);
        return;
    }
    for (int i = 0; i < operators.size(); i++) {
        if (!u[i]) {
            tmp.push_back(operators[i]);
            u[i] = true;
            permute(n, results, operators, tmp, u);
            tmp.pop_back();
            u[i] = false;
        }
    }
}

int main() {
    int n;
    cin >> n;
    vector<int> numbers(n, 0);
    vector<int> operators;
    for (int i = 0; i < n; i++) {
        cin >> numbers[i];
    }
    for (int i = 0; i < 4; i++) {
        int count;
        cin >> count;
        for (int j = 0; j < count; j++)
            operators.push_back(i);
    }
    vector<vector<int>> exps;
    vector<int> tmp;
    vector<bool> u(operators.size(), false);
    permute(n - 1, exps, operators, tmp, u);
    int answer[2] = {-1000000001, 1000000001};
    for (int i = 0; i < exps.size(); i++) {
        int v = numbers[0];
        for (int j = 0; j < n - 1; j++) {
            if (exps[i][j] == PLUS) {
                v += numbers[j + 1];
                continue;
            }
            if (exps[i][j] == MINUS) {
                v -= numbers[j + 1];
                continue;
            }
            if (exps[i][j] == MULT) {
                v *= numbers[j + 1];
                continue;
            }
            if (exps[i][j] == DIV) {
                v /= numbers[j + 1];
                continue;
            }
        }
        answer[0] = max(answer[0], v);
        answer[1] = min(answer[1], v);
    }
    cout << answer[0] << endl << answer[1] << endl;
}


