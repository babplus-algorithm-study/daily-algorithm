```
#include <iostream>
#include <vector>
#include <climits>
#include <algorithm>
#include <map>

using namespace std;

vector<int> v;
int arr[1001][1001];
int n, m, k;

int main() {
    cin >> n >> m;

    vector<string> patterns(n);
    map<string, int> pattern_count;

    for (int i = 0; i < n; i++) {
        string a;
        cin >> a;
        patterns[i] = a;
        pattern_count[a]++;

        for (int j = 0; j < m; j++) {
            arr[i][j] = a[j] - '0';
        }
    }

    cin >> k;

    int max_on_rows = 0;

    for (auto& p : pattern_count) {
        string pattern = p.first;
        int count = p.second;
        int zero_count = 0;

        for (char ch : pattern) {
            if (ch == '0') zero_count++;
        }

        if (zero_count <= k && (k - zero_count) % 2 == 0) {
            max_on_rows = max(max_on_rows, count);
        }
    }

    cout << max_on_rows << endl;

    return 0;
}

```
