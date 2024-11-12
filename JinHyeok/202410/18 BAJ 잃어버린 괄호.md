```
#include <iostream>
#include <algorithm>
using namespace std;

string a;
bool minus1;
int num, sum;

int main() {

	cin >> a;

	for (int i = 0; i <= a.size(); i++) {
		if (a[i] == '-' || a[i] == '+' || i == a.size()) {
			if (minus1 == true) {
				sum -= num;
				num = 0;
			}
			else {
				sum += num;
				num = 0;
			}
			if (a[i] == '-') {
				minus1 = true;
			}
		}
		else {
			num *= 10;
			num += a[i] - '0';
		}
	}

	cout << sum;

	return 0;
}
```
