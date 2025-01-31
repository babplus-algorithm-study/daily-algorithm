```
#include<iostream>
#include <algorithm>
#define MAX 0x3f3f3f3f
 
using namespace std;
int village[401][401];
 
int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
 
	int V, E, i, j, k;
	cin >> V >> E;
	for (i = 1; i <= V; i++)
		fill(village[i] + 1, village[i] + V + 1, MAX);
 
	int a, b, c;
	while (E--) {
		cin >> a >> b >> c;
		village[a][b] = c;
	}
	for (k = 1; k <= V; k++) {
		for (i = 1; i <= V; i++) {
			for (j = 1; j <= V; j++) {
				village[i][j] = min(village[i][j], village[i][k] + village[k][j]);
			}
		}
	}
	int min = MAX;
	for (i = 1; i <= V; i++) {
		if (village[i][i] < min)
			min = village[i][i];
	}
	if (min == MAX)
		cout << -1;
	else
		cout << min;
}
```
