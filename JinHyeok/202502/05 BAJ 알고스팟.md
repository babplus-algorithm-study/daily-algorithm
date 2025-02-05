```
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <climits>
using namespace std;

int M, N;
int dx[4] = { 0,0,-1,1 };
int dy[4] = { 1,-1,0,0 };

int d[103][103];
string board[102];
int answer = INT_MAX;
queue<pair<int, int>> q;


void dfs(int x, int y) {

    q.push({ x,y });

    while (!q.empty()) {

        auto cur = q.front();
        q.pop();
        for (int i = 0; i < 4; i++) {
            int nx = cur.first + dx[i];
            int ny = cur.second + dy[i];
            if (nx < 0 || nx >= N || ny < 0 || ny >= M) continue;

            if (board[nx][ny] == '0') {
                if (d[nx][ny] > d[cur.first][cur.second]) {
                    d[nx][ny] = d[cur.first][cur.second];
                    q.push({ nx,ny });
                }
            }
            else {
                if (d[nx][ny] > d[cur.first][cur.second] + 1) {
                    d[nx][ny] = d[cur.first][cur.second] + 1;
                    q.push({ nx,ny });
                }
            }
        }
    }
}
int main() {

    ios::sync_with_stdio(0);
    cin.tie(0);


    cin >> M >> N;
    for (int i = 0; i < N; i++) {
        cin >> board[i];
    }

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            d[i][j] = INT_MAX;
        }
    }

    d[0][0] = 0;

    dfs(0, 0);


    cout << d[N - 1][M - 1];

    return 0;
}
```
