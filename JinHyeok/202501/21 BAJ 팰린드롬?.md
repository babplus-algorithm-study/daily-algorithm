```
#include<iostream>
#include<algorithm>
using namespace std;

int dp[2001][2001];
int num[2001];
int N, M;
int s, e;

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);

	cin >> N;
	for (int i = 1; i <= N; i++)
	{
		cin >> num[i];
		dp[i][i] = 1;

		if (i != 1 && num[i - 1] == num[i])
			dp[i - 1][i] = 1;
	}


	for (int i = 2; i <= N - 1; i++)
	{
		for (int j = 1; i + j <= N; j++)
		{
			if (num[j] == num[i + j] && dp[j + 1][i + j - 1] == 1)
				dp[j][i + j] = 1;
		}
	}

	cin >> M;

	for (int i = 0; i < M; i++)
	{
		cin >> s >> e;

		cout << dp[s][e] << '\n';
	}

}
```
