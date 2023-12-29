#include <string>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <queue>
#include <iostream>
#define X 0
#define Y 1
using namespace std;
typedef vector<vector<int>> matrix;
typedef unordered_map<int, int> i2imap;
typedef pair<int, int> pos;

const int OIL = 1;
const int EMPTY = 0;
const int CHECKED = -1;

int compress(int x, int y, int m) {
    return x * m + y;
}

void analyze(int xs, int ys, matrix& land, 
             int oid, i2imap& c2oid, i2imap& oid2q) {
    int d[4][2] = {{0, 1}, {-1, 0}, {0, -1}, {1, 0}};
    int n = land.size();
    int m = land[0].size();
    land[xs][ys] = CHECKED;
    queue<pos> q;
    q.push(pos{xs, ys});
    int quantity = 1;
    c2oid[compress(xs, ys, m)] = oid;
    while (!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();
        for (int i = 0; i < 4; i++) {
            int nx = x + d[i][X];
            int ny = y + d[i][Y];
            if (nx > -1 && nx < n && ny > -1 && ny < m && land[nx][ny] == OIL) {
                q.push(pos{nx, ny});
                quantity++;
                land[nx][ny] = CHECKED;
                c2oid[compress(nx, ny, m)] = oid;
            }
        }
    }
    oid2q[oid] = quantity;
}

int solution(vector<vector<int>> land) {
    int answer = 0;
    unordered_map<int, int> c2oid; // coordinate -> oil id
    unordered_map<int, int> oid2q; // oil id -> quantity
    int n = land.size();
    int m = land[0].size();
    // O(n * m)
    int oid = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (land[i][j] == OIL) {
                analyze(i, j, land, oid, c2oid, oid2q);
                oid++;
            }
        }
    }
    // O(n * m) <= 10,000
    for (int y = 0; y < m; y++) {
        unordered_set<int> oilChunks;
        for (int x = 0; x < n; x++) {
            if(land[x][y] == CHECKED) {
                oilChunks.insert(c2oid[compress(x, y, m)]);
            }
        }
        int quantity = 0;
        for (const auto& oid : oilChunks) {
            quantity += oid2q[oid];
        }
        answer = max(answer, quantity);
    }
    return answer;
}
