```
#include<iostream>
using namespace std;

int arr[200];
int dp[200];
int max_num;

int main(void) {

	ios::sync_with_stdio(false);
	cin.tie(0);

	int n;
	cin >> n;

	for (int i = 0; i < n; i++){
		cin >> arr[i];
	}

	for (int i = 0; i < n; i++) {
		dp[i] = 1;
		for (int j = 0; j < i; j++) {
			if (arr[i] > arr[j] && dp[i] < dp[j] + 1) {
				dp[i]++;
			}
		}
		if (max_num < dp[i]) max_num = dp[i];

	}

	cout << n - max_num << '\n';

	return 0;
}
```
