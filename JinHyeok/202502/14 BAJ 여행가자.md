```
#include<iostream>
#include<algorithm>
#include<string>
#include<cstring>
#include<stack>
#include<queue>
#include<vector>
using namespace std;

int n,m,cnt;
int p[201];

int find(int x){
	if(p[x] == x) return x;
	return p[x] = find(p[x]);
}

void union_node(int x, int y){
	x = find(x);
	y = find(y);
	if(x < y) p[y] = x;
	else p[x] = y;
}

int main(void) {
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);
	
	cin >> n >> m;
	
	for(int i=1; i<=n; i++) p[i] = i;
	
	for(int i=1; i<=n; i++){
		for(int j=1; j<=n; j++){
			int x;
			cin >> x;
			if(x == 1) {
				union_node(i,j);
			}
		}
	}
	int root;
	for(int i=0; i<m; i++){
		int x;
		cin >> x;
		if(i == 0) root = find(x);
		else{
			if(find(root) != find(x)){
				cout << "NO";
				return 0;
			}
		}
	}
	cout << "YES";
	return 0;
}
```
