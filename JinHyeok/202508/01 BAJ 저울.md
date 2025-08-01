```
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int N, M;
    cin >> N >> M;

    vector<vector<bool>> heavier(N + 1, vector<bool>(N + 1, false));

    for (int i = 0; i < M; i++) {
        int a, b;
        cin >> a >> b;
        heavier[a][b] = true;
    }

    for (int k = 1; k <= N; k++) {
        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= N; j++) {
                if (heavier[i][k] && heavier[k][j]) {
                    heavier[i][j] = true;
                }
            }
        }
    }

    for (int i = 1; i <= N; i++) {
        int cnt = 0;
        for (int j = 1; j <= N; j++) {
            if (i == j) continue;
            if (!heavier[i][j] && !heavier[j][i]) cnt++;
        }
        cout << cnt << '\n';
    }

    return 0;
}

```
