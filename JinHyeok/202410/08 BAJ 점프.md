```
#include <iostream>
using namespace std;

int N,result;
int arr[101][101];
long long dp[101][101];

bool canGo(int x, int y) {
	return x >= 0 && x < N && y >= 0 && y < N;
}

int main() {

	cin >> N;

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cin >> arr[i][j];
		}
	}

	dp[0][0] = 1;

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {

			if (arr[i][j] == 0) continue;

			if (dp[i][j] != 0) {
				int next_i = i + arr[i][j];
				int next_j = j + arr[i][j];

				if (next_i < N) {
					dp[next_i][j] += dp[i][j];
				}
				if (next_j < N) {
					dp[i][next_j] += dp[i][j];
				}

			}
		}
	}

	cout << dp[N - 1][N - 1];

	return 0;
}
```
