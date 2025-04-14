```
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int N;
    cin >> N;

    vector<int> cranes(N);
    for (int i = 0; i < N; ++i) {
        cin >> cranes[i];
    }

    int M;
    cin >> M;

    vector<int> boxes(M);
    for (int i = 0; i < M; ++i) {
        cin >> boxes[i];
    }

    sort(cranes.rbegin(), cranes.rend());
    sort(boxes.rbegin(), boxes.rend());

    if (boxes[0] > cranes[0]) {
        cout << -1 << endl;
        return 0;
    }

    int time = 0;
    vector<bool> moved(M, false);
    int movedCount = 0;

    while (movedCount < M) {
        int boxIdx = 0;
        for (int i = 0; i < N;) {
            while (boxIdx < M) {
                if (!moved[boxIdx] && cranes[i] >= boxes[boxIdx]) {
                    moved[boxIdx] = true;
                    ++movedCount;
                    ++boxIdx;
                    break;
                }
                ++boxIdx;
            }
            ++i;
        }
        ++time;
    }

    cout << time << endl;

    return 0;
}

```
