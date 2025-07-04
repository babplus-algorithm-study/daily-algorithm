```
#include <iostream>
#include <vector>

using namespace std;

int main() {
    int N, M;
    cin >> N >> M;

    vector<int> vip(M);
    for (int i = 0; i < M; i++) {
        cin >> vip[i];
    }

    vector<int> dp(41);
    dp[0] = 1;
    dp[1] = 1;
    for (int i = 2; i <= N; i++) {
        dp[i] = dp[i - 1] + dp[i - 2];
    }

    int prev = 0;
    int result = 1;

    for (int i = 0; i < M; i++) {
        int gap = vip[i] - prev - 1;
        result *= dp[gap];
        prev = vip[i];
    }

    result *= dp[N - prev];

    cout << result << '\n';

    return 0;
}

```
