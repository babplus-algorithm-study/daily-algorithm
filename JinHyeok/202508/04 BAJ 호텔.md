```
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int C, N;
    cin >> C >> N;

    vector<pair<int, int>> city(N);
    for (int i = 0; i < N; i++) {
        cin >> city[i].first >> city[i].second;
    }

    vector<int> dp(C + 101, 1e9);
    dp[0] = 0;

    for (int i = 0; i <= C + 100; i++) {
        for (int j = 0; j < N; j++) {
            int cost = city[j].first;
            int customer = city[j].second;
            if (i >= customer) {
                dp[i] = min(dp[i], dp[i - customer] + cost);
            }
        }
    }

    int answer = 1e9;
    for (int i = C; i <= C + 100; i++) {
        answer = min(answer, dp[i]);
    }

    cout << answer << '\n';
    return 0;
}


```
