```
#include <iostream>
#include <vector>
using namespace std;



int main() {

	int n;
	cin >> n;
	
	vector<int> v;

	for (int i = 0; i < n; i++) {
		int a;
		cin >> a;
		v.push_back(a);
	}

	int answer = 0;

	while (1) {

		int cnt = 0;

		for (int i = 0; i < n; i++) {
			if (v[i] % 2 == 1) {
				v[i]--;
				answer++;
			}
		}

		for (int i = 0; i < n; i++) {
			if (v[i] == 0) {
				cnt++;
			}
		}

		if (cnt == n) {
			break;
		}

		for (int i = 0; i < n; i++) {
			v[i] /= 2;
		}
		answer++;

	}

	cout << answer;

	return 0;
}
```
