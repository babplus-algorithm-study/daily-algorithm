```
#include <iostream>
using namespace std;

int N, arr[8], used[8], perm[8], ans = 0;

void check() {
    int tmp = 0;
    for (int i = 0; i < N; i++) {
        int sum = 0;
        for (int j = i; ; j++) {
            sum += perm[j % N];
            if (sum > 50) break;
            if (sum == 50) {
                tmp++;
                break;
            }
        }
    }
    if (tmp > ans) ans = tmp;
}

void dfs(int depth) {
    if (depth == N) {
        check();
        return;
    }

    for (int i = 0; i < N; i++) {
        if (!used[i]) {
            used[i] = 1;
            perm[depth] = arr[i];
            dfs(depth + 1);
            used[i] = 0;
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> arr[i];
    }

    dfs(0);

    cout << ans / 2 << "\n";
    return 0;
}

```
