#include <vector>
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main() {
    int n;
    long long answer = 0;
    cin >> n;
    vector<long long> distances(n, 0);
    vector<long long> prices(n, 0);
    for (int i = 0; i < n - 1; i++)
        cin >> distances[i];
    for (int i = 0; i < n; i++)
        cin >> prices[i];
    long long minprice = prices[0];
    for (int i = 0; i < n - 1; i++) {
        minprice = min(minprice, prices[i]);
        answer += minprice * distances[i];
    }
    cout << answer << endl;
    return 0;
}
