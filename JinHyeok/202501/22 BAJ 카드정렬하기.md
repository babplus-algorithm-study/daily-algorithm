```
#include <iostream>
#include <queue>
using namespace std;

int n;
int ans;
priority_queue<int, vector<int>, greater<int>> pq;

int main(void) {

	cin >> n;

	if (n == 1) {
		cout << 0 << endl;
		return 0;
	}
	int tmp;
	for (int i = 0; i < n; i++) {
		cin >> tmp;
		pq.push(tmp);
	}

	while (!pq.empty()) {
		int sum = 0;
		sum += pq.top();
		pq.pop();
		if (!pq.empty()) {
			sum += pq.top();
			pq.pop();
			if (!pq.empty())
				pq.push(sum);
		}
		ans += sum;
	}

	cout << ans << endl;

	return 0;
}

```
