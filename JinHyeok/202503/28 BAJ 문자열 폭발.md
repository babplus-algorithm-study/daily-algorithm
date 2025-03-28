```
#include <iostream>
#include <string>
#include <stack>

using namespace std;

int main() {
    string str, bomb;
    cin >> str >> bomb;

    string result;
    int bombLen = bomb.size();

    for (char ch : str) {
        result.push_back(ch);

        if (result.size() >= bombLen && result.substr(result.size() - bombLen) == bomb) {
            result.erase(result.end() - bombLen, result.end());
        }
    }

    if (result.empty()) {
        cout << "FRULA" << "\n";
    }
    else {
        cout << result << "\n";
    }

    return 0;
}

```
