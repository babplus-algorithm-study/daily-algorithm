```
#include <iostream>
#include <queue>
#include <algorithm>
#include <climits>
using namespace std;


int n, m, x, y, k;
int arr[21][21];
queue<int> q;

//    2
// 4 1 3
//    5
//    6
// 1 4 3 2 5 6
vector<int> dice(6);
int dirX[5] = {0, 0,  0, -1, 1};
int dirY[5] = {0, 1, -1,  0, 0};

bool canGo(int x, int y) {
	return x >= 0 && x < n && y >= 0 && y < m;
}

//    2
// 1 3 6
//    5
//    4
// 3 1 6 2 5 4
void rollEast() {
	int temp = dice[0];
	dice[0] = dice[2];
	dice[2] = dice[5];
	dice[5] = dice[1];
	dice[1] = temp;
}

//    2
// 4 1 3
//    5
//    6
// 1 4 3 2 5 6

//    2
// 6 4 1
//    5
//    3
// 4 6 1 2 5 3

void rollWest() {
	int temp = dice[0];
	dice[0] = dice[1];
	dice[1] = dice[5];
	dice[5] = dice[2];
	dice[2] = temp;
}

//    2
// 4 1 3
//    5
//    6
// 1 4 3 2 5 6

//    6
// 4 2 3
//    1
//    5
// 2 4 3 6 1 5

void rollNorth() {
	int temp = dice[0];
	dice[0] = dice[3];
	dice[3] = dice[5];
	dice[5] = dice[4];
	dice[4] = temp;
}

//    2
// 4 1 3
//    5
//    6
// 1 4 3 2 5 6

//    1
// 4 5 3
//    6
//    2
// 5 4 3 1 6 2

void rollSouth() {
	int temp = dice[0];
	dice[0] = dice[4];
	dice[4] = dice[5];
	dice[5] = dice[3];
	dice[3] = temp;
}



int main() {

	cin >> n >> m >> x >> y >> k;

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			int a;
			cin >> a;
			arr[i][j] = a;
		}
	}

	for (int i = 0; i < k; i++) {
		int b;
		cin >> b;
		q.push(b);
	}

	int curX = x;
	int curY = y;

	while (!q.empty()) {
		int f = q.front();
		q.pop();
		curX = curX + dirX[f];
		curY = curY + dirY[f];


		if (canGo(curX, curY)) {
			/*cout << curX << " " << curY << "\n";
			cout << arr[curX][curY] << "\n";*/
			if (f == 1) {
				rollEast();
			}
			else if (f == 2) {
				rollWest();
			}
			else if (f == 3) {
				rollNorth();
			}
			else {
				rollSouth();
			}
			if (arr[curX][curY] == 0) {
				arr[curX][curY] = dice[0];
			}
			else {
				dice[0] = arr[curX][curY];
				arr[curX][curY] = 0;
			}

			cout << dice[5] << "\n";
		}
		else {
			curX = curX - dirX[f];
			curY = curY - dirY[f];
		}
	}

	return 0;
}
```
