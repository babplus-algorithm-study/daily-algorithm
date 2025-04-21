```
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N;
int inning[50][9];
int maxScore = 0;

int playGame(vector<int> &order) {
    int score = 0;
    int idx = 0;

    for (int i = 0; i < N; ++i) {
        int outCount = 0;
        bool base[3] = {false, false, false};
        while (outCount < 3) {
            int player = order[idx];
            int result = inning[i][player];

            if (result == 0) {
                outCount++;
            } else {
                for (int b = 2; b >= 0; --b) {
                    if (base[b]) {
                        if (b + result >= 3) {
                            score++;
                        } else {
                            base[b + result] = true;
                        }
                        base[b] = false;
                    }
                }

                if (result == 4) {
                    score++;
                } else {
                    base[result - 1] = true;
                }
            }
            idx = (idx + 1) % 9;
        }
    }
    return score;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    cin >> N;
    for (int i = 0; i < N; ++i)
        for (int j = 0; j < 9; ++j)
            cin >> inning[i][j];

    vector<int> players = {1, 2, 3, 4, 5, 6, 7, 8};

    do {
        vector<int> order(9);
        int idx = 0;
        for (int i = 0; i < 9; ++i) {
            if (i == 3) {
                order[i] = 0;
            } else {
                order[i] = players[idx++];
            }
        }
        maxScore = max(maxScore, playGame(order));
    } while (next_permutation(players.begin(), players.end()));

    cout << maxScore << '\n';
    return 0;
}
```
