```
#include <iostream>
#include <queue>
#include <algorithm>
#include <climits>
using namespace std;


int n;
int arr[51][51];
queue<pair<int,int>> q;
int dx[4] = { 0,0,-1,1 };
int dy[4] = { -1,1, 0,0 };
int visited[51][51];

bool canGo(int x, int y) {
	return x >= 0 && x < n && y >= 0 && y < n;
}

void bfs(int a, int b) {
	q.push({ a,b });
	visited[a][b] = 0;

	while (!q.empty()) {

		int x = q.front().first;
		int y = q.front().second;
		q.pop();

		for (int i = 0; i < 4; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];

			if (canGo(nx, ny)) {
				if (arr[nx][ny] == 1) {
					if (visited[nx][ny] > visited[x][y]) {
						visited[nx][ny] = visited[x][y];
						q.push({ nx,ny });
					}
				}
				else {
					if (visited[nx][ny] > visited[x][y] + 1) {
						visited[nx][ny] = visited[x][y] + 1;
						q.push({ nx,ny });
					}
				}
			}
		}
	}
}

int main() {

	cin >> n;

	for (int i = 0; i < n; i++) {
		string a;
		cin >> a;
		for (int j = 0; j < a.size(); j++) {
			arr[i][j] = a[j] - '0';
		}
	}
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			visited[i][j] = INT_MAX;
		}
	}

	bfs(0, 0);
	
	cout << visited[n - 1][n - 1];

	return 0;
}
```
