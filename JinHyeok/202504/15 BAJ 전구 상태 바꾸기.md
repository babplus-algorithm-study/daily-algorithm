```
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int colorToInt(char c) {
    if (c == 'R') return 0;
    if (c == 'G') return 1;
    return 2;
}

int rotate(int color) {
    return (color + 1) % 3;
}

int minOperations(string s, int target) {
    int n = s.size();
    vector<int> bulbs(n);
    for (int i = 0; i < n; ++i) {
        bulbs[i] = colorToInt(s[i]);
    }

    int count = 0;
    for (int i = 0; i <= n - 3; ++i) {
        if (bulbs[i] != target) {
            int diff = (target - bulbs[i] + 3) % 3;
            for (int j = 0; j < 3; ++j) {
                bulbs[i + j] = (bulbs[i + j] + diff) % 3;
            }
            count += diff;
        }
    }

    for (int i = n - 2; i < n; ++i) {
        if (bulbs[i] != target) return -1;
    }

    return count;
}

int main() {
    int n;
    string s;
    cin >> n >> s;

    int res = -1;
    for (int target = 0; target < 3; ++target) {
        int op = minOperations(s, target);
        if (op != -1) {
            if (res == -1 || op < res) res = op;
        }
    }

    cout << res << endl;
    return 0;
}

```
