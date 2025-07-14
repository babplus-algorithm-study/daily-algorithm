```
#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

int N, W;
int open1, open2;
vector<int> useOrder;
int dp[21][21][21];

int solve(int index, int door1, int door2) {
    if (index == W) return 0;

    int& ret = dp[index][door1][door2];
    if (ret != -1) return ret;

    int target = useOrder[index];

    int move1 = solve(index + 1, target, door2) + abs(door1 - target);
    int move2 = solve(index + 1, door1, target) + abs(door2 - target);

    return ret = min(move1, move2);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N;
    cin >> open1 >> open2;
    cin >> W;

    useOrder.resize(W);
    for (int i = 0; i < W; i++) {
        cin >> useOrder[i];
    }

    for (int i = 0; i <= 20; i++)
        for (int j = 0; j <= 20; j++)
            for (int k = 0; k <= 20; k++)
                dp[i][j][k] = -1;

    cout << solve(0, open1, open2) << '\n';

    return 0;
}

```
