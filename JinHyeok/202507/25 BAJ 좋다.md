```
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int N;
    cin >> N;

    vector<long long> A(N);
    for (int i = 0; i < N; ++i)
        cin >> A[i];

    sort(A.begin(), A.end());

    int count = 0;

    for (int k = 0; k < N; ++k) {
        int i = 0, j = N - 1;

        while (i < j) {
            if (i == k) {
                ++i;
                continue;
            }
            if (j == k) {
                --j;
                continue;
            }

            long long sum = A[i] + A[j];

            if (sum == A[k]) {
                ++count;
                break;
            } else if (sum < A[k]) {
                ++i;
            } else {
                --j;
            }
        }
    }

    cout << count;
    return 0;
}

```
