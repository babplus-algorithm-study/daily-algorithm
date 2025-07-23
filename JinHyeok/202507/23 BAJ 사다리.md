```
#include <iostream>
#include <cmath>
using namespace std;

double x, y, c;

double getHeight(double len, double width) {
    return sqrt(len * len - width * width);
}

bool isPossible(double width) {
    double h1 = getHeight(x, width);
    double h2 = getHeight(y, width);
    double meet = (h1 * h2) / (h1 + h2);
    return meet >= c;
}

int main() {
    cin >> x >> y >> c;

    double low = 0;
    double high = min(x, y);
    double mid;

    for (int i = 0; i < 100; ++i) {
        mid = (low + high) / 2;
        if (isPossible(mid)) {
            low = mid;
        } else {
            high = mid;
        }
    }

    cout.precision(10);
    cout << fixed << mid << endl;

    return 0;
}


```
