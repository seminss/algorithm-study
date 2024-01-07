#include <vector>
#include <iostream>
#include <string>
#include <sstream>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    vector<int> numbers(n, 0);
    vector<int> partialSumTo(n, 0);
    int psum = 0;
    for (int i = 0; i < n; i++) {
        cin >> numbers[i];
        psum += numbers[i];
        partialSumTo[i] = psum;
    }
    ostringstream oss;
    for (int i = 0; i < m; i++) {
        int s, e;
        cin >> s >> e;
        oss << partialSumTo[e - 1] - partialSumTo[s - 2] << endl;
    }
    cout << oss.str();
    return 0;
}
