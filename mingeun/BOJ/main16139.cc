#include <vector>
#include <iostream>
#include <string>
#include <sstream>
#include <stdio.h>
using namespace std;

int main() {
    string s;
    int n;
    cin >> s >> n;
    char c;
    int l, r;
    vector<vector<int>> count(s.length(), vector<int>(26, 0));
    for (int i = 0; i < s.length(); i++) {
        for (int j = 0; j < 26; j++) {
            if (i > 0){
                count[i][j] = count[i - 1][j];
            }
            if (j + 'a' == s[i])
                count[i][j]++;
        }
    }
    ostringstream oss;
    for (int i = 0; i < n; i++) {
        cin >> c >> l >> r;
        if (l == 0) 
            oss << count[r][c - 'a'] << endl;
        else 
            oss << count[r][c - 'a'] - count[l- 1][c - 'a'] << endl;
    }
    cout << oss.str();
    for (int i= 0; i < 26; i++) {
        printf("%c ", i + 'a');
        for (int j = 0; j < s.length(); j++) {
            printf("%d ", count[j][i]);
        }
        printf("\n");
    }
    return 0;
}
