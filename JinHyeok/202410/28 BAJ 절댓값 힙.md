```
#include <iostream>
#include <queue>
#include <cmath>
using namespace std;

struct Compare {
	bool operator()(int a, int b) {
		if (abs(a) == abs(b)) {
			return a > b;
		}
		return abs(a) > abs(b);
	}
};

priority_queue<int, vector<int>, Compare> pq;
int n,a;


int main() {

	ios::sync_with_stdio(0);
	cin.tie(0);

	cin >> n;

	for (int i = 0; i < n; i++) {
		cin >> a;

		if (a == 0) {
			if (pq.empty()) {
				cout << 0 << "\n";
			}
			else {
				int b = pq.top();
				cout << b << "\n";
				pq.pop();
			}
		}
		else {
			pq.push(a);
		}
	}

	return 0;
}
```
