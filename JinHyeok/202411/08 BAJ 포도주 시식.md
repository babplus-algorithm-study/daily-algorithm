```
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> v(10001);
int dp[10001];

int main() {

	int n;
	cin >> n;

	for (int i = 1; i <= n; i++) {
		int a;
		cin >> a;
		v[i] = a;
	}


	dp[0] = 0;
	dp[1] = v[1];
	dp[2] = v[1] + v[2];

	// 6 6 13 10 9 8 1

	for (int i = 3; i <= n; i++) {
		dp[i] = max({ dp[i - 3] + v[i - 1] + v[i], dp[i - 2] + v[i], dp[i - 1] });
	}

	cout << dp[n];


	return 0;
}
```
