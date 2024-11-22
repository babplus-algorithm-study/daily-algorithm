```
#include <iostream>
#include <algorithm>
#include <queue>
#include <cstring>
using namespace std;

vector<long long> v;

int main() {
    int N;
    cin >> N;


    queue<long long> q;

    for (int i = 0; i <= 9; i++) {
        q.push(i);
        v.push_back(i);
    }


    while (!q.empty()) {
        long long num = q.front();
        int last = num % 10;
        q.pop();
        for (int i = 0; i < last; i++) {
            long long newnum = num * 10 + i;
            q.push(newnum);
            v.push_back(newnum);
        }
    }
    if (N > v.size()) {
        cout << -1;
    }
    else {
        cout << v[N - 1];
    }


    return 0;
}
```
