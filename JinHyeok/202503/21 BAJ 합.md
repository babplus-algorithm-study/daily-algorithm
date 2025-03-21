```
#include <iostream>

using namespace std;

long long digitSumTo(long long n) {
    if (n <= 0) return 0;

    long long count[10] = { 0 }, factor = 1, totalSum = 0;
    long long temp, remainder;

    while (n > 0) {
        temp = n / (factor * 10);
        remainder = n % (factor * 10);

        for (int i = 0; i < 10; i++) count[i] += temp * factor;
        for (int i = 1; i <= remainder / factor; i++) count[i] += factor;
        count[(remainder / factor + 1) % 10] += remainder % factor;

        n -= 9 * factor;
        factor *= 10;
    }

    for (int i = 1; i < 10; i++) totalSum += i * count[i];

    return totalSum;
}

int main() {
    long long L, U;
    cin >> L >> U;

    cout << digitSumTo(U) - digitSumTo(L - 1) << endl;

    return 0;
}

```
