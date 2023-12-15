#include <iostream>
#include <ostream>
#include <utility>
#include <cstdlib>
#include <vector>
#include <queue>
using namespace std;

enum Direction {
    UP, DOWN, LEFT, RIGHT
};

typedef pair<unsigned int, unsigned int> pos;

class Board {
    public:
        Board(vector<vector<int>>&& matrix) : board(std::move(matrix)), n(matrix.size()) {  }
        Board(const Board& other) : board(other.board), n(other.n) {  }
        Board movedBoard(Direction d);
        friend ostream& operator <<(ostream& os, const Board& board);
        int findLargestNumber();
    private:
        int n;
        vector<vector<int>> board;
        void moveRow(int r, Direction d);
        void moveColumn(int c, Direction d);
};

void dfs(vector<Direction>& directions, Board board, int& m);

int main() {
    cin.tie(NULL);
    cout.tie(NULL);
    ios::sync_with_stdio(false);

    int n;
    cin >> n;
    vector<vector<int>> matrix(n, vector<int>(n, 0));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> matrix[i][j];
        }
    }
    Board board(std::move(matrix));
    // test
    vector<Direction> directions{};
    int m  = 0;
    dfs(directions, board, m);
    cout << m << endl;
    return 0;
}

void dfs(vector<Direction>& directions, Board board, int& m) {
    if (directions.size() == 5) {
        int tmp = board.findLargestNumber();
        m = (m < tmp) ? tmp : m;
        return;
    }
    for (int i = UP; i <= RIGHT; ++i) {
        Direction currentDir = static_cast<Direction>(i);
        directions.push_back(currentDir);
        dfs(directions, board.movedBoard(currentDir), m);
        directions.pop_back();
    }
    return;
}

int Board::findLargestNumber() {
    int m = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            m = (board[i][j] > m) ? board[i][j] : m;
        }
    }
    return m;
}

ostream& operator <<(ostream& os, const Board& board) {
    os << endl << "\033[32m";
    for (const auto& row : board.board) {
        for (int value : row) {
            os << value << " ";
        }
        os << endl;
    }
    os << "\033[0m";
    return os;
}

Board Board::movedBoard(Direction d) {
    Board result(*this);
    if (d == Direction::RIGHT || d == Direction::LEFT) {
        for (int i = 0; i < n; i++) {
            result.moveRow(i, d);
        }
    }
    if (d == Direction::UP || d == Direction::DOWN) {
        for (int i = 0; i < n; i++) {
            result.moveColumn(i, d);
        }
    }
    return result;
}

void Board::moveRow(int r, Direction d) {
    queue<int> q1;
    vector<int> v;
    if (d == Direction::LEFT) {
        for (int i = 0; i < n; i++) {
            if (board[r][i] == 0) {
                continue;
            }
            if (q1.empty()) {
                q1.push(board[r][i]);
                board[r][i] = 0;
                continue;
            }
            if (q1.back() == board[r][i]) {
                int tmp = q1.back();
                q1.pop();
                v.push_back(tmp + board[r][i]);
                board[r][i] = 0;
                continue;
            }
            if (q1.back() != board[r][i]) {
                int tmp = q1.back();
                q1.pop();
                v.push_back(tmp);
                q1.push(board[r][i]);
                board[r][i] = 0;
                continue;
            }
        }
        while (!q1.empty()) {
            int tmp = q1.front();
            q1.pop();
            v.push_back(tmp);
        }
        for (int i = 0; i < v.size(); i++) {
            board[r][i] = v[i];
        }
        return;
    }
    if (d == Direction::RIGHT) {
        for (int i = n - 1; i >= 0; i--) {
            if (board[r][i] == 0) {
                continue;
            }
            if (q1.empty()) {
                q1.push(board[r][i]);
                board[r][i] = 0;
                continue;
            }
            if (q1.back() == board[r][i]) {
                int tmp = q1.back();
                q1.pop();
                v.push_back(tmp + board[r][i]);
                board[r][i] = 0;
                continue;
            }
            if (q1.back() != board[r][i]) {
                int tmp = q1.back();
                q1.pop();
                v.push_back(tmp);
                q1.push(board[r][i]);
                board[r][i] = 0;
                continue;
            }
        }
        while (!q1.empty()) {
            int tmp = q1.front();
            q1.pop();
            v.push_back(tmp);
        }
        for (int i = 0; i < v.size(); i++) {
            board[r][n- 1 - i] = v[i];
        }
        return;
    }
}

void Board::moveColumn(int c, Direction d) {
    queue<int> q1;
    vector<int> v;
    if (d == Direction::UP) {
        for (int i = 0; i < n; i++) {
            if (board[i][c] == 0) {
                continue;
            }
            if (q1.empty()) {
                q1.push(board[i][c]);
                board[i][c] = 0;
                continue;
            }
            if (q1.back() == board[i][c]) {
                int tmp = q1.back();
                q1.pop();
                v.push_back(tmp + board[i][c]);
                board[i][c] = 0;
                continue;
            }
            if (q1.back() != board[i][c]) {
                int tmp = q1.back();
                q1.pop();
                v.push_back(tmp);
                q1.push(board[i][c]);
                board[i][c] = 0;
                continue;
            }
        }
        while (!q1.empty()) {
            int tmp = q1.front();
            q1.pop();
            v.push_back(tmp);
        }
        for (int i = 0; i < v.size(); i++) {
            board[i][c] = v[i];
        }
        return;
    }
    if (d == Direction::DOWN) {
        for (int i = n - 1; i >= 0; i--) {
            if (board[i][c] == 0) {
                continue;
            }
            if (q1.empty()) {
                q1.push(board[i][c]);
                board[i][c] = 0;
                continue;
            }
            if (q1.back() == board[i][c]) {
                int tmp = q1.back();
                q1.pop();
                v.push_back(tmp + board[i][c]);
                board[i][c] = 0;
                continue;
            }
            if (q1.back() != board[i][c]) {
                int tmp = q1.back();
                q1.pop();
                v.push_back(tmp);
                q1.push(board[i][c]);
                board[i][c] = 0;
                continue;
            }
        }
        while (!q1.empty()) {
            int tmp = q1.front();
            q1.pop();
            v.push_back(tmp);
        }
        for (int i = 0; i < v.size(); i++) {
            board[n- 1 - i][c] = v[i];
        }
        return;
    }
}

