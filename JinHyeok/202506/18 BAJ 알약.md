```
#include <iostream>
#include <vector>
using namespace std;


int main() {

    vector<long long> v(31);
    v[0] = 1;

    for (int i = 1; i <= 30; i++) {
        for (int j = 0; j < i; j++) {
            v[i] += v[j] * v[i - 1 - j];
        }
    }

    int N;
    while (cin >> N && N != 0) {
        cout << v[N] << "\n";
    }

    return 0;
}

```
