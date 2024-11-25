```
#include <iostream>
#include <queue>
using namespace std;


int n, m;
char arr[101][101];
bool visited[101][101];
int dx[4] = {0,0,1,-1};
int dy[4] = {-1,1,0,0};
int cnt = 0;
int w_sum = 0;
int b_sum = 0;
char flag;

bool canGo(int x, int y) {
	return x >= 0 && x < m && y >= 0 && y < n;
}


void bfs(int a, int b) {

	queue<pair<int,int>> q;
	q.push({ a,b });
	visited[a][b] = true;
	cnt = 1;

	while (!q.empty()) {

		int x = q.front().first;
		int y = q.front().second;
		q.pop();

		for (int i = 0; i < 4; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];

			if (canGo(nx, ny) && !visited[nx][ny] && arr[nx][ny] == flag) {
				visited[nx][ny] = true;
				q.push({ nx,ny });
				cnt++;
			}
		}
	}
}

int main() {
	cin >> n >> m;

	for (int i = 0; i < m; i++) {
		string a;
		cin >> a;
		for (int j = 0; j < a.size(); j++) {
			arr[i][j] = a[j];
		}
	}

	for (int i = 0; i < m; i++) {
		for (int j = 0; j < n; j++) {
			if (visited[i][j] == false && arr[i][j] == 'W') {
				flag = 'W';
				bfs(i, j);
				w_sum += (cnt * cnt);
			}
		}
	}

	for (int i = 0; i < m; i++) {
		for (int j = 0; j < n; j++) {
			if (visited[i][j] == false && arr[i][j] == 'B') {
				flag = 'B';
				bfs(i, j);
				b_sum += (cnt * cnt);
			}
		}
	}

	cout << w_sum << " " << b_sum;


}
```
