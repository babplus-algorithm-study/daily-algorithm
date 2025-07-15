```
#include <iostream>
#include <queue>
using namespace std;

int n;
char grid[100][100];
bool visited[100][100];
int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};

void bfs(int x, int y, bool colorBlind) {
    queue<pair<int, int>> q;
    q.push({x, y});
    visited[x][y] = true;
    char current = grid[x][y];

    while (!q.empty()) {
        int cx = q.front().first;
        int cy = q.front().second;
        q.pop();

        for (int i = 0; i < 4; i++) {
            int nx = cx + dx[i];
            int ny = cy + dy[i];

            if (nx < 0 || ny < 0 || nx >= n || ny >= n) continue;
            if (visited[nx][ny]) continue;

            char next = grid[nx][ny];
            if (colorBlind) {
                if ((current == 'R' || current == 'G') && (next == 'R' || next == 'G')) {
                    visited[nx][ny] = true;
                    q.push({nx, ny});
                } else if (current == 'B' && next == 'B') {
                    visited[nx][ny] = true;
                    q.push({nx, ny});
                }
            } else {
                if (current == next) {
                    visited[nx][ny] = true;
                    q.push({nx, ny});
                }
            }
        }
    }
}

int countRegion(bool colorBlind) {
    int count = 0;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            visited[i][j] = false;

    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            if (!visited[i][j]) {
                bfs(i, j, colorBlind);
                count++;
            }

    return count;
}

int main() {
    cin >> n;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            cin >> grid[i][j];

    int normal = countRegion(false);
    int blind = countRegion(true);

    cout << normal << " " << blind << endl;
}

```
