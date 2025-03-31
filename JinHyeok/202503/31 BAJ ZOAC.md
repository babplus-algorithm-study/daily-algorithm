```
#include <iostream>
using namespace std;

string s;
bool visited[101];
void backtracking(int start, int end) {
    if (start == end) return;
    char c = '~';
    int idx = 0;
    for (int i = start; i < end; i++) {
        if (s[i] < c) {
            c = s[i];
            idx = i;
        }
    }
    visited[idx] = 1;
    for (int i = 0; i < s.length(); i++) {
        if (visited[i]) cout << s[i];
    }
    cout << '\n';
    backtracking(idx + 1, end);
    backtracking(start, idx);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    cin >> s;
    backtracking(0, s.length());
}
```
