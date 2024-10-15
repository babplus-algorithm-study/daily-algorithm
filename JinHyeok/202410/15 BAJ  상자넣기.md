```
#include <iostream>
#include <algorithm>
using namespace std;

int n;
int arr[1001];
int dp[1001];
int result = 1;

int main() {

	cin >> n;

	fill(dp, dp + n, 1);

	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < i; j++) {
			if (arr[i] > arr[j]) {
				dp[i] = max(dp[i], dp[j] + 1);
				result = max(result, dp[i]);
			}
		}
	}

	cout << result;

	return 0;
}
```
