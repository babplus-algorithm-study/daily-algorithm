```
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<string> v(n);

    for (int i = 0; i < n; i++) {
        cin >> v[i];
    }

    sort(v.begin(), v.end());

    int count = n;

    for (int i = 1; i < n; i++) {
        if (v[i].substr(0, v[i - 1].size()) == v[i - 1]) {
            count--;
        }
    }

    cout << count << endl;

    return 0;
}

```
