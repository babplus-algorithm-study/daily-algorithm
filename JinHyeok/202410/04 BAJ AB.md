```
#include <iostream>

using namespace std;

void solve(int N, int K)
{
    if (K > (N / 2) * (N / 2 + N % 2))
    {
        cout << -1;
    }
    else if (K == 0)
    {
        for (int i = 0; i < N - 1; i++)
            cout << 'B';
        cout << 'A';
    }
    else
    {
        for (int i = 0, j = 1, sum = 0; i < N; i++)
        {
            if (N - j - i > 0 && sum + N - j - i <= K)
            {
                cout << 'A';
                sum += N - j++ - i;
            }
            else
                cout << 'B';
        }
    }
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N, K;
    cin >> N >> K;
    solve(N, K);
}
```
