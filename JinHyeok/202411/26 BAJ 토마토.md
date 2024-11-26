```
#include <iostream>
#include <queue>
using namespace std;

int n, m;
int arr[1001][1001];
int dx[4] = { 0, 0, -1, 1 };
int dy[4] = { 1, -1, 0, 0 };

bool canGo(int x, int y) {
    return x >= 0 && x < m && y >= 0 && y < n;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n >> m;

    queue<pair<int, int>> q;
    int emptyCells = 0;

    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            cin >> arr[i][j];
            if (arr[i][j] == 1) {
                q.push({ i, j });
            }
            else if (arr[i][j] == 0) {
                emptyCells++;
            }
        }
    }

    if (emptyCells == 0) {
        cout << 0;
        return 0;
    }

    int answer = 0;

    while (!q.empty()) {
        int size = q.size();
        for (int i = 0; i < size; i++) {
            int x = q.front().first;
            int y = q.front().second;
            q.pop();

            for (int k = 0; k < 4; k++) {
                int nx = x + dx[k];
                int ny = y + dy[k];

                if (canGo(nx, ny) && arr[nx][ny] == 0) {
                    arr[nx][ny] = 1;
                    q.push({ nx, ny });
                    emptyCells--;
                }
            }
        }

        if (!q.empty()) {
            answer++;
        }
    }

    
    cout << (emptyCells == 0 ? answer : -1);
    return 0;
}

```
