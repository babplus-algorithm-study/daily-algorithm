```
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int N, K;
    cin >> N >> K;

    vector<int> sensors(N);
    for (int i = 0; i < N; i++) {
        cin >> sensors[i];
    }
    
    sort(sensors.begin(), sensors.end());

    vector<int> diffs;
    for (int i = 1; i < N; i++) {
        diffs.push_back(sensors[i] - sensors[i - 1]);
    }

    sort(diffs.begin(), diffs.end(), greater<int>());

    int answer = 0;
    for (int i = K - 1; i < diffs.size(); i++) {
        answer += diffs[i];
    }

    cout << answer << endl;
    return 0;
}

```
