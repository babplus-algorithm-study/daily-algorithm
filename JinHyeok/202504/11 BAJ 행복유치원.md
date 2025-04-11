```
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int N, K;
    cin >> N >> K;
    vector<int> heights(N);
    
    for (int i = 0; i < N; ++i) {
        cin >> heights[i];
    }

    vector<int> diffs;
    for (int i = 1; i < N; ++i) {
        diffs.push_back(heights[i] - heights[i - 1]);
    }

    sort(diffs.rbegin(), diffs.rend());

    int total_cost = heights[N - 1] - heights[0];

    for (int i = 0; i < K - 1; ++i) {
        total_cost -= diffs[i];
    }

    cout << total_cost << endl;
    return 0;
}


```
