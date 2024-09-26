```
#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>
using namespace std;

int N;
string a;
int arr[26][26];
bool visited[26][26];
queue<pair<int,int>> q;
vector<int> result;
int dx[4] = { 0, 0,1,-1 };
int dy[4] = { 1,-1,0, 0 };
int cnt;

bool canGo(int x, int y) {
	return x >= 0 && x < N && y >= 0 && y < N;
}

void bfs(int num1, int num2) {
	q.push({ num1, num2 });
	visited[num1][num2] = true;
	cnt++;

	while (!q.empty()) {
		int x = q.front().first;
		int y = q.front().second;
		q.pop();


		for (int i = 0; i < 4; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];
			if (canGo(nx, ny) && arr[nx][ny] == 1 && !visited[nx][ny]) {
				cnt++;
				visited[nx][ny] = true;
				q.push({ nx,ny });
			}
		}
	}

	result.push_back(cnt);
	cnt = 0;
}

int main() {

	ios::sync_with_stdio(0);
	cin.tie(0);

	cin >> N;

	for (int i = 0; i < N; i++) {
		cin >> a;
		for (int j = 0; j < a.size(); j++) {
			arr[i][j] = a[j] - '0';
		}
	}
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			if (arr[i][j] == 1 && visited[i][j] == false) {
				bfs(i, j);
			}
		}
	}
	cout << result.size() << "\n";
	sort(result.begin(), result.end());
	for (int i = 0; i < result.size(); i++) {
		cout << result[i] << "\n";
	}
}
```
