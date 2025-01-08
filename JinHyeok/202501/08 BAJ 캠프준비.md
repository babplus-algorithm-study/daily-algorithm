```
#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>
using namespace std;

int N, L, R, X;
vector<int> v;
int answer = 0;

void solve(int idx, int count, int sum, int minDiff, int maxDiff) {

    if (count >= 2 && sum >= L && sum <= R && (maxDiff - minDiff) >= X) {
        answer++;
    }

    for (int i = idx; i < N; i++) {
        solve(i + 1, count + 1, sum + v[i], min(minDiff, v[i]), max(maxDiff, v[i]));
    }
}

int main() {
    cin >> N >> L >> R >> X;
    v.resize(N);

    for (int i = 0; i < N; i++) {
        cin >> v[i];
    }

    solve(0, 0, 0, INT_MAX, 0);

    cout << answer << endl;

    return 0;
}

```
