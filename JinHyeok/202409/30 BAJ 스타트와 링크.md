```
#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <climits>
using namespace std;

int n;
int arr[21][21];
bool team[21];
int min_diff = INT_MAX;

void backtracking(int idx, int cnt) {
    if (cnt == n / 2) {
        int start_team = 0, link_team = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (team[i] && team[j]) {
                    start_team += arr[i][j];
                }
                else if (!team[i] && !team[j]) {
                    link_team += arr[i][j];
                }
            }
        }

        int diff = abs(start_team - link_team);
        min_diff = min(min_diff, diff);
        return;
    }

    if (idx >= n) return;

    team[idx] = true;
    backtracking(idx + 1, cnt + 1);

    team[idx] = false;
    backtracking(idx + 1, cnt);
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);


    cin >> n;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> arr[i][j];
        }
    }

    backtracking(0, 0);

    cout << min_diff << '\n';

    return 0;
}

```
