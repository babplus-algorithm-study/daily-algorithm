```
#include <iostream>
#include <string>
using namespace std;

bool isPalindrome(string s, int left, int right) {
    while (left < right) {
        if (s[left] != s[right]) return false;
        left++;
        right--;
    }
    return true;
}

int check(string s) {
    int left = 0;
    int right = s.length() - 1;

    while (left < right) {
        if (s[left] == s[right]) {
            left++;
            right--;
        }
        else {
            if (isPalindrome(s, left + 1, right) || isPalindrome(s, left, right - 1))
                return 1;
            else
                return 2;
        }
    }
    return 0;
}

int main() {
    int T;
    cin >> T;

    for (int i = 0; i < T; i++) {
        string s;
        cin >> s;
        cout << check(s) << endl;
    }

    return 0;
}

```
