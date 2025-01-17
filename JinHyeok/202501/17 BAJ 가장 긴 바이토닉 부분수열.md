```
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> v;
int left_size[1001];
int right_size[1001];
int answer;

int main() {

	int n;
	cin >> n;


	for (int i = 0; i < n; i++) {
		int a;
		cin >> a;
		v.push_back(a);
	}

	for (int i = 0; i < n; i++) {
		int a;
		cin >> a;
		v.push_back(a);
	}

	for (int i = 0; i < n; i++) {
		left_size[i] = 1;
		right_size[i] = 1;
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < i; j++) {
			if (v[i] > v[j]) {
				left_size[i] = max(left_size[i], left_size[j] + 1);
			}
		}
	}

	for (int i = n - 1; i >= 0; i--) {
		for (int j = n-1; j > i; j--) {
			if (v[i] > v[j]) {
				right_size[i] = max(right_size[i], right_size[j] + 1);
			}
		}
	}

	for (int i = 0; i < n; i++) {
		answer = max(answer, left_size[i] + right_size[i]);
	}


	cout << answer - 1;

	return 0;
}
```
