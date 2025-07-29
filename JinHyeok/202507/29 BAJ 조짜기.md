```
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int N;
    cin >> N;

    vector<int> score(N);
    for (int i = 0; i < N; ++i) {
        cin >> score[i];
    }

    vector<int> dp(N + 1, 0);

    for (int i = 1; i <= N; ++i) {
        int maxScore = score[i - 1];
        int minScore = score[i - 1];

        for (int j = i - 1; j >= 0; --j) {
            maxScore = max(maxScore, score[j]);
            minScore = min(minScore, score[j]);
            dp[i] = max(dp[i], dp[j] + (maxScore - minScore));
        }
    }

    cout << dp[N] << '\n';
    return 0;
}

```
