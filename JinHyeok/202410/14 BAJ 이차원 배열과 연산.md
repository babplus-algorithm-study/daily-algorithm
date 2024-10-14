```
#include <iostream>
#include <vector>
#include <algorithm>
#include <utility>
using namespace std;

int board[101][101];
int freq[101];
int row = 3, col = 3, sec = 0;

bool cmp(pair<int, int> n1, pair<int, int> n2) {
    if (n1.second == n2.second) {
        return n1.first < n2.first;
    }
    else {
        return n1.second < n2.second;
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int r, c, k;
    cin >> r >> c >> k;

    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            cin >> board[i][j];
        }
    }

    while (true) {
        if (board[r - 1][c - 1] == k) {
            break;
        }
        if (sec == 100) {
            sec = -1;
            break;
        }

        int first, second;
        if (row >= col) {
            first = row;
            second = col;
        }
        else {
            first = col;
            second = row;
        }

        vector<int> l(first);
        for (int i = 0; i < first; i++) {
            fill(freq, freq + 101, 0);
            vector<pair<int, int>> sf;

            for (int j = 0; j < second; j++) {
                if (row >= col) {
                    freq[board[i][j]]++;
                }
                else {
                    freq[board[j][i]]++;
                }
            }

            for (int j = 1; j <= 100; j++) {
                if (freq[j] != 0) {
                    sf.push_back({ j, freq[j] });
                }
            }

            sort(sf.begin(), sf.end(), cmp);

            for (int j = 0; j < sf.size() && j < 50; j++) {
                if (row >= col) {
                    board[i][j * 2] = sf[j].first;
                    board[i][j * 2 + 1] = sf[j].second;
                }
                else {
                    board[j * 2][i] = sf[j].first;
                    board[j * 2 + 1][i] = sf[j].second;
                }
            }

            l[i] = (sf.size() >= 50) ? 100 : sf.size() * 2;
        }

        second = *max_element(l.begin(), l.end());

        for (int i = 0; i < first; i++) {
            for (int j = l[i]; j < second; j++) {
                if (row >= col) {
                    board[i][j] = 0;
                }
                else {
                    board[j][i] = 0;
                }
            }
        }

        if (row >= col) {
            col = second;
        }
        else {
            row = second;
        }

        sec++;
    }

    cout << sec;
}

```
