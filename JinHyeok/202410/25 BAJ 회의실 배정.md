```
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int n, k, l;
vector<pair<int, int>> office;


int main() {


	cin >> n;

	for (int i = 0; i < n; i++) {
		cin >> k >> l;

		office.push_back({ l,k });
	}

	sort(office.begin(), office.end());

	int meeting = office[0].first;
	int answer = 1;
	for (int i = 1; i < office.size(); i++) {
		if (meeting <= office[i].second) {
			answer++;
			meeting = office[i].first;
		}
	}

	cout << answer;


	return 0;
}
```
