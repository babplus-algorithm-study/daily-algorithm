```
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N;
vector<pair<int, int>> eggs;
int maxBroken = 0;

void backtrack(int index) {
    if (index == N) {
        int brokenCount = 0;
        for (int i = 0; i < N; i++) {
            if (eggs[i].first <= 0) brokenCount++;
        }
        maxBroken = max(maxBroken, brokenCount);
        return;
    }

    if (eggs[index].first <= 0) {
        backtrack(index + 1);
        return;
    }

    bool hit = false;

    for (int i = 0; i < N; i++) {
        if (i == index || eggs[i].first <= 0) continue;

        eggs[index].first -= eggs[i].second;
        eggs[i].first -= eggs[index].second;

        hit = true;
        backtrack(index + 1);

        eggs[index].first += eggs[i].second;
        eggs[i].first += eggs[index].second;
    }

    if (!hit) backtrack(index + 1);
}

int main() {
    cin >> N;
    eggs.resize(N);

    for (int i = 0; i < N; i++) {
        cin >> eggs[i].first >> eggs[i].second;
    }

    backtrack(0);
    cout << maxBroken << endl;

    return 0;
}

```
