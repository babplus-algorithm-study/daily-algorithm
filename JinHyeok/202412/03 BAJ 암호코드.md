```
#include <iostream>
#include <queue>
#include <string>
using namespace std;

int dp[5001];


int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    string a;

    cin >> a;

    if (a[0] == '0') {
        cout << 0;
        return 0;
    }

    dp[0] = 1;
    dp[1] = 1;

    
    for (int i = 2; i <= a.size(); i++) {
        string b = "";
        bool size_check = false;

        b += a[i - 2];
        b += a[i - 1];

        int c = stoi(b);

        if (c == 0) {
            cout << 0;
            return 0;
        }

        if (c < 10) {
            dp[i] = dp[i - 1] % 1000000;
            continue;
        }

        if (c % 10 == 0) {
            if (c > 26) {
                cout << 0;
                return 0;
            }
            else {
                dp[i] = dp[i - 2] % 1000000;
            }
        }
        else if (c > 26) {
            dp[i] = dp[i - 1] % 1000000;
        }
        else {
            dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000;
        }
    }

    cout << dp[a.size()];



    return 0;
}

```
