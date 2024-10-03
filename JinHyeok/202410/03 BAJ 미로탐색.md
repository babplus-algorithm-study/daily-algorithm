```
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int n,m;
queue<pair<int,int>> q;
vector<int> v;
string a;
int dx[4] = { 0,0,-1,1 };
int dy[4] = { -1,1,0,0 };
bool visited[101][101];
int arr[101][101];
int dist[101][101];
int cnt;

bool canGo(int x, int y) {
	return x >= 0 && x < n && y >= 0 && y < m;
}

void bfs(int x, int y) {
	q.push({ x, y });
	visited[x][y] = true;

	while (!q.empty()) {
		int x = q.front().first;
		int y = q.front().second;
		q.pop();

		for (int i = 0; i < 4; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];

			if (canGo(nx, ny) && arr[nx][ny] && !visited[nx][ny]) {
				visited[nx][ny] = true;
				q.push({ nx,ny });
				dist[nx][ny] = dist[x][y] + 1;
			}
		}
	}
}


int main() {

	cin >> n >> m;


	for (int i = 0; i < n; i++) {
		cin >> a;
		for (int j = 0; j < m; j++) {
			arr[i][j] = a[j] - '0';
		}
	}

	bfs(0, 0);

	cout << dist[n-1][m-1] + 1;

	return 0;
}
```
