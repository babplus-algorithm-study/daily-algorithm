```
#include <iostream>
#include <queue>
using namespace std;

struct Data {
    int a, b, c;
};

int A, B, C;
bool chk[202][202], ans[202];

void bfs() {
    queue<Data> q;
    q.push({ 0, 0, C });

    while (!q.empty()) {
        Data now = q.front();
        q.pop();

        if (chk[now.a][now.b])
            continue;

        chk[now.a][now.b] = true;

        if (now.a == 0)
            ans[now.c] = true;

        if (now.a + now.b > B)
            q.push({ (now.a + now.b) - B, B, now.c });
        else
            q.push({ 0, now.a + now.b, now.c });

        if (now.a + now.c > C)
            q.push({ (now.a + now.b) - C, now.b, C });
        else
            q.push({ 0, now.b, now.a + now.c });

        if (now.b + now.a > A)
            q.push({ A, (now.b + now.a) - A, now.c });
        else
            q.push({ now.b + now.a, 0, now.c });

        if (now.b + now.c > C)
            q.push({ now.a, (now.b + now.c) - C, C });
        else
            q.push({ now.a, 0, now.b + now.c });

        if (now.c + now.a > A)
            q.push({ A, now.b, (now.c + now.a) - A });
        else
            q.push({ now.c + now.a, now.b, 0 });

        if (now.c + now.b > B)
            q.push({ now.a, B, (now.c + now.b) - B });
        else
            q.push({ now.a, now.c + now.b, 0 });
    }
}

void print() {
    for (int i = 0; i <= C; i++) {
        if (ans[i])
            cout << i << " ";
    }
}

int main() {
    cin >> A >> B >> C;
    bfs();
    print();
    return 0;
}

```
