```
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int emoticon(int S) {

    vector<vector<bool>> visited(1001, vector<bool>(1001, false));
    queue<pair<int, int>> q;
    queue<int> time;

    q.push({ 1, 0 });
    time.push(0);
    visited[1][0] = true;

    while (!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;
        int cur = time.front();
        q.pop();
        time.pop();

        if (x == S) return cur;

        if (!visited[x][x]) {
            q.push({ x, x });
            time.push(cur + 1);
            visited[x][x] = true;
        }

        int newx = x + y;
        if (y > 0 && newx <= 1000 && !visited[newx][y]) {
            q.push({ newx, y });
            time.push(cur + 1);
            visited[newx][y] = true;
        }

        if (x > 1 && !visited[x - 1][y]) {
            q.push({ x - 1, y });
            time.push(cur + 1);
            visited[x - 1][y] = true;
        }
    }

    return -1;
}

int main() {
    int S;
    cin >> S;
    cout << emoticon(S) << endl;
    return 0;
}

```
