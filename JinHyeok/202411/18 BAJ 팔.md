```
#include <iostream>
#include <string>
#include <algorithm>
#include <climits>
using namespace std;


int main() {

	string l, r;
	cin >> l >> r;
	int answer = INT_MAX;

	if (r.size() != l.size()) {
		answer = 0;
	}
	else {
		int cnt = 0;
		for (int i = 0; i < l.size(); i++) {
			if (l[i] == '8' || r[i] == '8') {
				if (l[i] == r[i]) {
					cnt++;
				}
				else {
					break;
				}
			}
			else {
				if (l[i] == r[i]) {
					continue;
				}
				else {
					break;
				}
			}
		}
		answer = cnt;
	}

	cout << answer;

	return 0;
}
```
