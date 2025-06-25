```
#include <iostream>
#include <string>
using namespace std;

bool isPalindrome(const string& s) {
    int left = 0;
    int right = s.size() - 1;
    while (left < right) {
        if (s[left] != s[right]) return false;
        left++;
        right--;
    }
    return true;
}

int main() {
    string s;
    cin >> s;
    int n = s.size();

    if (!isPalindrome(s)) {
        cout << n << endl;
    } else {
        bool allSame = true;
        for (int i = 1; i < n; i++) {
            if (s[i] != s[0]) {
                allSame = false;
                break;
            }
        }
        if (allSame) {
            cout << -1 << endl;
        } else {
            cout << n - 1 << endl;
        }
    }

    return 0;
}

```
