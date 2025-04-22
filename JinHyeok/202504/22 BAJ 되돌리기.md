```
#include <iostream>
#include <vector>
#include <string>
#include <utility>
#include <cstdlib>

using namespace std;

int commandCount;
vector<pair<string, int>> history;

string getTextAt(int targetTime) {
    for (int i = history.size() - 1; i >= 0; i--) {
        if (targetTime > history[i].second) {
            return history[i].first;
        }
    }
    return "";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> commandCount;
    for (int i = 0; i < commandCount; i++) {
        string operation, value;
        int timestamp;
        cin >> operation >> value >> timestamp;

        if (operation == "type") {
            string currentText = history.empty() ? value : history.back().first + value;
            history.push_back({currentText, timestamp});
        } else {
            int undoDuration = stoi(value);
            string restoredText = getTextAt(timestamp - undoDuration);
            history.push_back({restoredText, timestamp});
        }
    }

    cout << history.back().first;
}

```
