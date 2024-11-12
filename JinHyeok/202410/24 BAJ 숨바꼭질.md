```
#include <iostream>
#include <cmath>
#include <queue>
#include <algorithm>
using namespace std;

int n, k, answer;
queue<pair<int, int>> q;
bool visited[100001];

void bfs(int n, int cnt) {

	q.push({ n,cnt });
	visited[n] = true;

	while (!q.empty()) {

		int cur = q.front().first;
		int tmp = q.front().second;
		q.pop();

		if (cur == k) {
			cout << tmp;
			return;
		}

		if (cur + 1 <= 100000 && cur + 1 >= 0 && !visited[cur + 1]) {
			q.push({ cur + 1, tmp + 1 });
			visited[cur + 1] = true;
		}
		if (cur - 1 <= 100000 && cur - 1 >= 0 && !visited[cur - 1]) {
			q.push({ cur - 1, tmp + 1 });
			visited[cur - 1] = true;
		}
		if (cur * 2 <= 100000 && cur * 2 >= 0 && !visited[cur * 2]) {
			q.push({ cur * 2, tmp + 1 });
			visited[cur * 2] = true;
		}
	}
}


int main() {

	cin >> n >> k;

	bfs(n, 0);

	return 0;
}
```
