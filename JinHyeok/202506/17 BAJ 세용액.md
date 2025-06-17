```
#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>
#include <cstdlib>

using namespace std;

int main() {
    int N;
    cin >> N;

    vector<int> arr(N);
    for (int i = 0; i < N; i++) cin >> arr[i];

    sort(arr.begin(), arr.end());

    long long closestSum = LLONG_MAX;
    int ans1 = 0, ans2 = 0, ans3 = 0;

    for (int i = 0; i < N - 2; i++) {
        int left = i + 1;
        int right = N - 1;

        while (left < right) {
            long long sum = (long long)arr[i] + arr[left] + arr[right];

            if (llabs(sum) < llabs(closestSum)) {
                closestSum = sum;
                ans1 = arr[i];
                ans2 = arr[left];
                ans3 = arr[right];
            }

            if (sum < 0) {
                left++;
            }
            else {
                right--;
            }
        }
    }

    vector<int> result = { ans1, ans2, ans3 };
    sort(result.begin(), result.end());

    for (int i = 0; i < 3; i++) {
        cout << result[i] << " ";
    }
    cout << '\n';

    return 0;
}

```
