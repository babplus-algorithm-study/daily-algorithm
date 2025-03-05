```
#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int N, M;
vector<string> A;

bool isCheck(long long num) {
    if (num < 0) return false;
    long long root = sqrt(num);
    return root * root == num;
}

int main() {
    cin >> N >> M;
    A.resize(N);

    for (int i = 0; i < N; i++) {
        cin >> A[i];
    }

    int answer = -1;

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {


            for (int k = -N; k < N; k++) {
                for (int l = -M; l < M; l++) {
                    if (k == 0 && l == 0) continue;

                    long long num = 0;
                    int x = i, y = j;

                    while (x >= 0 && x < N && y >= 0 && y < M) {
                        num = num * 10 + (A[x][y] - '0');

                        if (isCheck(num)) {
                            answer = max(answer, (int)num);
                        }

                        x += k;
                        y += l;
                    }
                }
            }
        }
    }

    cout << answer << "\n";

    return 0;
}

```
