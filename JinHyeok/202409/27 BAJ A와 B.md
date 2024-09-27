```
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

string a, b;

int main() {

	ios::sync_with_stdio(0);
	cin.tie(0);

	cin >> a >> b;
	int total_size = b.size() - a.size();

	for (int i = 0; i < total_size; i++) {
		if (b[b.size() - 1] == 'A') {
			b.erase(b.size() - 1);
		}
		else {
			b.erase(b.size() - 1);
			reverse(b.begin(), b.end());
		}			
	}

	if (a == b) {
		cout << 1;
	}
	else {
		cout << 0;
	}

	return 0;
}
```
