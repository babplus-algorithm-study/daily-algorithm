```
#include <iostream>
#include <queue>
#include <tuple>
#include <algorithm>
using namespace std;

struct State {
    int a, b, c, cnt;
};

int visited[61][61][61];

int attack[6][3] = {
    {9, 3, 1}, {9, 1, 3},
    {3, 9, 1}, {3, 1, 9},
    {1, 9, 3}, {1, 3, 9}
};

int bfs(int a, int b, int c) {
    queue<State> q;
    q.push({ a, b, c, 0 });
    visited[a][b][c] = 1;

    while (!q.empty()) {
        State cur = q.front();
        q.pop();

        if (cur.a == 0 && cur.b == 0 && cur.c == 0) {
            return cur.cnt;
        }

        for (int i = 0; i < 6; i++) {
            int na = max(0, cur.a - attack[i][0]);
            int nb = max(0, cur.b - attack[i][1]);
            int nc = max(0, cur.c - attack[i][2]);

            if (!visited[na][nb][nc]) {
                visited[na][nb][nc] = 1;
                q.push({ na, nb, nc, cur.cnt + 1 });
            }
        }
    }
    return -1;
}

int main() {
    int n;
    cin >> n;

    int scv[3] = { 0, 0, 0 };
    for (int i = 0; i < n; i++) {
        cin >> scv[i]; 
    }

    cout << bfs(scv[0], scv[1], scv[2]) << '\n';

    return 0;
}

```
