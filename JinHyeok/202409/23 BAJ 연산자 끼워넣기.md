#include <iostream>
#include <vector>
#include <climits>
using namespace std;

int n;
vector<int> number;
vector<int> calculate;
int calMax = INT_MIN;
int calMin = INT_MAX;

void calMaxMin(int result, int num) {

	if (num == n) {
		if (result > calMax) {
			calMax = result;
		}
		if (result < calMin) {
			calMin = result;
		}
		return;
	}

	for (int i = 0; i < 4; i++) {
		if (calculate[i] > 0) {
			calculate[i]--;
			if (i == 0)
				calMaxMin(result + number[num], num + 1);
			else if (i == 1)
				calMaxMin(result - number[num], num + 1);
			else if (i == 2)
				calMaxMin(result * number[num], num + 1);
			else
				calMaxMin(result / number[num], num + 1);
			calculate[i]++;
		}
	}
	return;

}



int main() {

	cin >> n;

	for (int i = 0; i < n; i++) {
		int a;
		cin >> a;
		number.push_back(a);
	}

	for (int i = 0; i < 4; i++) {
		int b;
		cin >> b;
		calculate.push_back(b);
	}

	calMaxMin(number[0], 1);

	cout << calMax << "\n";
	cout << calMin;
}
