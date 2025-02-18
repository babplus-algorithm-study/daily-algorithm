```
#include <iostream>

using namespace std;

pair<int, int> p1;
pair<int, int> p2;
pair<int, int> p3;

void solution() {
    int a = (p2.first - p1.first) * (p3.second - p1.second) - (p3.first - p1.first) * (p2.second - p1.second);

    if (a > 0) {
        cout << 1;
    }
    else if (a < 0) {
        cout << -1;
    }
    else {
        cout << 0;
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> p1.first >> p1.second;
    cin >> p2.first >> p2.second;
    cin >> p3.first >> p3.second;

    solution();

    return 0;
}
```
