```
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int T;
    cin >> T;

    while (T--) {
        int N;
        cin >> N;

        vector<int> coins(N);
        for (int i = 0; i < N; ++i) {
            cin >> coins[i];
        }

        int M;
        cin >> M;

        vector<int> dp(M + 1, 0);
        dp[0] = 1;

        for (int i = 0; i < N; ++i) {
            for (int j = coins[i]; j <= M; ++j) {
                dp[j] += dp[j - coins[i]];
            }
        }

        cout << dp[M] << endl;
    }

    return 0;
}

```
