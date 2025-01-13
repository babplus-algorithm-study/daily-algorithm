```
#include <iostream>
using namespace std;

int n = 0;

bool checked(int num) {

	for (int i = 2; i * i <= num; i++) {
		if (num % i == 0)
			return false;
	}
	return true;
}

void dfs(int num, int len) {
	if (len == n) {
		cout << num << "\n";
		return;
	}

	for (int i = 1; i <= 9; i++) {
		if (checked(num * 10 + i))
			dfs(num * 10 + i, len + 1);
	}

	return;
}

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0), cout.tie(0);

	cin >> n;
	dfs(2, 1);
	dfs(3, 1);
	dfs(5, 1);
	dfs(7, 1);

	return 0;
}
```
