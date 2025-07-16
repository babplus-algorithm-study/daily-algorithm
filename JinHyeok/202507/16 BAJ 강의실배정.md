```
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    vector<pair<int, int>> lectures(N);
    for (int i = 0; i < N; ++i) {
        cin >> lectures[i].first >> lectures[i].second;
    }

    sort(lectures.begin(), lectures.end());

    priority_queue<int, vector<int>, greater<int>> pq;

    for (int i = 0; i < N; ++i) {
        if (!pq.empty() && pq.top() <= lectures[i].first) {
            pq.pop();
        }
        pq.push(lectures[i].second);
    }

    cout << pq.size() << '\n';

    return 0;
}

.
```
