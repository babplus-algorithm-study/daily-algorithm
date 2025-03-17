```
#include <iostream>
#include <vector>
#include <climits>
#include <algorithm>
using namespace std;

vector<int> v;
int N;

int countMax(int num) {

	int count = 0;
	double curMax = INT_MAX;
	if (num != 0) {
		for (int i = num-1; i >= 0; i--) {
			double side = (double)(v[num] - v[i]) / (num - i);
			if (side < curMax) {
				count++;
				curMax = min(curMax, side);
			}
		}
	}
	double curMin = INT_MIN;

	if (num != N) {
		for (int i = num+1; i < N; i++) {
			double side = (double)(v[i] - v[num]) / (i - num);
			if (side > curMin) {
				count++;
				curMin = max(curMin, side);
			}
		}
	}

	return count;
}

int main() {

	cin >> N;

	for (int i = 0; i < N; i++) {
		int a;
		cin >> a;
		v.push_back(a);
	}
	int answer = 0;
	for (int i = 0; i < N; i++) {
		answer = max(answer, countMax(i));
	}
	

	cout << answer;

	return 0;
}
```
