```
#include <iostream>
#include <cmath>

using namespace std;


int gcd(int a, int b) {
    while (b != 0) {
        int temp = a % b;
        a = b;
        b = temp;
    }
    return a;
}

int main() {
    int n, m;
    cin >> n >> m;

    int target = m / n;
    int a = 1, b = target;

    for (int i = 1; i * i <= target; i++) {
        if (target % i == 0) {
            int x = i;
            int y = target / i;

            if (gcd(x, y) == 1) {
                a = x;
                b = y;
            }
        }
    }


    cout << a * n << " " << b * n << endl;

    return 0;
}

```
