```
#include <iostream>
#include <string>
using namespace std;

int N;
bool found = false;

bool check(const string &s) {
    int len = s.length();
    for (int i = 1; i <= len / 2; i++) {
        if (s.substr(len - i, i) == s.substr(len - 2 * i, i)) {
            return false;
        }
    }
    return true;
}

void dfs(string s) {
    if (found) return;

    if (s.length() == N) {
        cout << s << '\n';
        found = true;
        return;
    }

    for (char c = '1'; c <= '3'; c++) {
        s.push_back(c);
        if (check(s)) dfs(s);
        s.pop_back();
    }
}

int main() {
    cin >> N;
    dfs("");
    return 0;
}

```
