```
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int n, m;
vector<string> map;
int dx[4] = {0, 0, 1, -1};
int dy[4] = {1, -1, 0, 0};

// BFS를 이용하여 (x, y)에서 가장 먼 육지까지의 거리 반환
int bfs(int x, int y) {
    vector<vector<int>> dist(n, vector<int>(m, -1));
    queue<pair<int, int>> q;
    q.push({x, y});
    dist[x][y] = 0;
    int maxDist = 0;

    while (!q.empty()) {
        int cx = q.front().first;
        int cy = q.front().second;
        q.pop();

        for (int i = 0; i < 4; i++) {
            int nx = cx + dx[i];
            int ny = cy + dy[i];

            if (nx >= 0 && nx < n && ny >= 0 && ny < m && map[nx][ny] == 'L' && dist[nx][ny] == -1) {
                dist[nx][ny] = dist[cx][cy] + 1;
                maxDist = max(maxDist, dist[nx][ny]);
                q.push({nx, ny});
            }
        }
    }
    return maxDist;
}

int main() {
    cin >> n >> m;
    map.resize(n);

    for (int i = 0; i < n; i++) {
        cin >> map[i];
    }

    int result = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (map[i][j] == 'L') {
                result = max(result, bfs(i, j));
            }
        }
    }

    cout << result << endl;
    return 0;
}

```
