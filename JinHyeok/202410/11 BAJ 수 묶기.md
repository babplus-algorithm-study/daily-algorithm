```
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int N,a;
int result;
vector<int> v;
vector<int> w;

int main() {

	cin >> N;

	for (int i = 0; i < N; i++) {
		cin >> a;
		if(a > 0)
			v.push_back(a);
		else
			w.push_back(a);
	}

	sort(v.rbegin(), v.rend());
	sort(w.begin(), w.end());

	if (v.size() % 2 == 0) {
		for (int i = 0; i < v.size(); i += 2) {
			if (v[i] * v[i + 1] >= v[i] + v[i + 1]) {
				result += (v[i] * v[i + 1]);
			}
			else {
				result += (v[i] + v[i + 1]);
			}
		}
	}
	else {
		result += v[v.size() - 1];
		for (int i = 0; i < v.size() - 1; i += 2) {
			if (v[i] * v[i + 1] >= v[i] + v[i + 1]) {
				result += (v[i] * v[i + 1]);
			}
			else {
				result += (v[i] + v[i + 1]);
			}
		}
	}

	if (w.size() % 2 == 0) {
		for (int i = 0; i < w.size(); i+=2) {
			result += (w[i] * w[i + 1]);
		}
	}
	else {
		result += w[w.size() - 1];
		for (int i = 0; i < w.size() - 1; i += 2) {
			result += (w[i] * w[i + 1]);
		}
	}

	
	cout << result;


}
```
