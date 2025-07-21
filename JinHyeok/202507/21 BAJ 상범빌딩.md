```
#include <iostream>
#include <queue>
#include <tuple>
using namespace std;

int L, R, C;
char building[30][30][30];
bool visited[30][30][30];

int dl[6] = {1, -1, 0, 0, 0, 0};
int dr[6] = {0, 0, 1, -1, 0, 0};
int dc[6] = {0, 0, 0, 0, 1, -1};

struct Node {
    int l, r, c, dist;
};

int bfs(int sl, int sr, int sc) {
    queue<Node> q;
    q.push({sl, sr, sc, 0});
    visited[sl][sr][sc] = true;

    while (!q.empty()) {
        Node cur = q.front();
        q.pop();

        if (building[cur.l][cur.r][cur.c] == 'E') {
            return cur.dist;
        }

        for (int i = 0; i < 6; i++) {
            int nl = cur.l + dl[i];
            int nr = cur.r + dr[i];
            int nc = cur.c + dc[i];

            if (nl >= 0 && nl < L && nr >= 0 && nr < R && nc >= 0 && nc < C) {
                if (!visited[nl][nr][nc] && building[nl][nr][nc] != '#') {
                    visited[nl][nr][nc] = true;
                    q.push({nl, nr, nc, cur.dist + 1});
                }
            }
        }
    }

    return -1;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    while (true) {
        cin >> L >> R >> C;
        if (L == 0 && R == 0 && C == 0) break;

        int sl, sr, sc;

        for (int l = 0; l < L; l++) {
            for (int r = 0; r < R; r++) {
                for (int c = 0; c < C; c++) {
                    cin >> building[l][r][c];
                    if (building[l][r][c] == 'S') {
                        sl = l; sr = r; sc = c;
                    }
                    visited[l][r][c] = false;
                }
            }
            string dummy;
            getline(cin, dummy);
        }

        int result = bfs(sl, sr, sc);
        if (result == -1) {
            cout << "Trapped!\n";
        } else {
            cout << "Escaped in " << result << " minute(s).\n";
        }
    }

    return 0;
}

```
