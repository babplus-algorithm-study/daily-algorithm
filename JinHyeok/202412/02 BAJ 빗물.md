```
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
    int T;
    int N, M, K;
    int X, Y;
    int answer = 0;

    cin >> N >> M;

    vector<int> v(M);

    for (int i = 0; i < M; i++)
        cin >> v[i];

    for (int i = 1; i < M - 1; i++) {
        int left = 0; int right = 0;
        
        for (int j = 0; j < i; j++) left = max(left, v[j]);

        for (int j = M - 1; j > i; j--) right = max(right, v[j]);

        answer += max(0, min(left, right) - v[i]);
    }

    cout << answer << "\n";

    return 0;
}
```
