```
#include <iostream>
#include <cmath>
using namespace std;

int col[16];
int n;
int ans = 0;

void queen(int x) {
    if (n == x) {
        ans++;
    }
    else {
        for (int i = 0; i < n; i++) {
            col[x] = i;
            bool can = true;
            for (int j = 0; j < x; j++) {
                if (col[x] == col[j] || abs(col[x] - col[j]) == x - j) {
                    can = false;
                    break;
                }
            }
            if (can) {
                queen(x + 1);
            }
        }
    }
}

int main() {
    cin >> n;

    queen(0);

    cout << ans;

    return 0;
}

```
