```
#include <iostream>
using namespace std;

long long arr[1001];

int main(void) {
	int n, m, t;
	long long sum = 0;
	long long cnt = 0;

	cin >> n >> m;

	for (int i = 1; i <= n; i++) {
		cin >> t;
		sum += t;
		arr[sum % m]++;
	}

	for (int i = 0; i <= m; i++)
		cnt += ((arr[i] * (arr[i] - 1)) / 2);

	cout << arr[0] + cnt;

	return 0;
}
```
