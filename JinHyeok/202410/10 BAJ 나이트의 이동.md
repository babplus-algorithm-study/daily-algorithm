```
#include <iostream>
#include <queue>
using namespace std;
#define X first
#define Y second
int dx[8] = {2, -2, 2, -2, 1, 1, -1, -1};
int dy[8] = {1, 1, -1, -1, 2, -2, 2, -2};
int dist[305][305];
bool vis[305][305];

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
    
	int testCase, l;
	int x, y, xx, yy;
	cin >> testCase;
	for(int i = 0; i < testCase; i++) {
		
		cin >> l;
		for(int j = 0; j < l; j++) {
			fill(dist[j], dist[j] + l, 0);
			fill(vis[j], vis[j] + l, 0);
		}
		
		queue<pair<int,int>> Q;
		cin >> x >> y;
		Q.push({x, y});
		vis[x][y] = 1;		
		cin >> xx >> yy;
		while(!Q.empty()) {
			auto cur = Q.front(); Q.pop();
			for (int dir = 0; dir < 8; dir++) {
				int nx = cur.X + dx[dir];
				int ny = cur.Y + dy[dir];
				if (nx < 0 || nx >= l || ny < 0 || ny >= l) continue;
				if (vis[nx][ny]) continue;
				Q.push({nx, ny});
				vis[nx][ny] = 1;
				dist[nx][ny] = dist[cur.X][cur.Y] + 1;
			}
		} 
		cout << dist[xx][yy] << '\n';
	}
	
 	return 0;
}
```
