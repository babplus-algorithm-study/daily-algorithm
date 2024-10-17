```
#include <iostream>
#include <algorithm>
using namespace std;

int t, m, n, k, x, y, ans;
int field[50][50];
int xpos[4] = {0, 0, -1, 1};
int ypos[4] = {1, -1, 0, 0};

void dfs(int x, int y) {
	field[x][y] = 0;
	for (int i = 0; i < 4; i++) {
		int xx = x + xpos[i];
		int yy = y + ypos[i];
		if (xx < 0 || yy < 0 || xx >= m || yy >= n) continue;
		if (field[xx][yy] == 1) {
			dfs(xx, yy);
		}
	}
}

int main() {
	cin >> t;
	for (int q = 0; q < t; q++) {
		cin >> m >> n >> k;
		for (int i = 0; i < k; i++) {
			cin >> x >> y;
			field[x][y] = 1;
		}

		for (int i = 0; i < m; i++) {
			for (int j = 0; j < n; j++) {
				if (field[i][j] == 1) {
					dfs(i, j);
					ans++;
				}
			}
		}

		cout << ans << '\n';
		ans = 0;
		for (int i = 0; i < m; i++) {
			fill(field[i], field[i] + n, 0);
		}
	}
}
```
