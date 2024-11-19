```
#include <iostream>
#include <string>
#include <algorithm>
#include <climits>
using namespace std;

int btn[10];

bool check_possible(int r) {
		string a = to_string(r);
		for (int i = 0; i < a.size(); i++) {
			if (btn[a[i] - '0'] == 1) {
				return false;
			}
		}
		return true;
}

int main() {
	int n,m;
	cin >> n >> m;
	for (int i = 0; i < m; i++) {
		int a;
		cin >> a;
		btn[a] = 1;
	}

	int nogada = abs(n - 100);

	for (int i = 0; i <= 1000000; i++) {

		if (check_possible(i)) {
			string b = to_string(i);
			int possible = b.size() + abs(n - i);
			nogada = min(nogada, possible);
		}
	}
	cout << nogada;



	return 0;
}
```
