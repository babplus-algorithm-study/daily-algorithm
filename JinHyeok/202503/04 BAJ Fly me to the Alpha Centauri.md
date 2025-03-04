```
#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int t;
    cin >> t;

    for (int i = 0; i < t; i++) {
        long long x, y;
        cin >> x >> y;

        long long distance = y - x;
        long long maxStep = 0;

        while (maxStep * maxStep <= distance) {
            maxStep++;
        }
        maxStep--;

        long long minMoves = 2 * maxStep - 1;
        long long remainingDistance = distance - maxStep * maxStep;

        long long extraMoves = (long long)ceil((double)remainingDistance / maxStep);
        minMoves += extraMoves;

        cout << minMoves << endl;
    }

    return 0;
}

```
