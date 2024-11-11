```
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

int l, c;
vector<char> v;
vector<string> answer;
vector<int> ind;

int main() {

    cin >> l >> c;

    vector<bool> mask(c);

    for (int i = 0; i < c; i++) {
        char a;
        cin >> a;
        v.push_back(a);
    }

    sort(v.begin(), v.end());

    // a c i s t w

    fill(mask.end() - l, mask.end(), true);

    do {
        string combination = "";
        for (int i = 0; i < c; i++) {
            if (mask[i]) {
                combination += v[i];
            }
        }
        answer.push_back(combination);

    } while (next_permutation(mask.begin(), mask.end()));

    sort(answer.begin(), answer.end());

    for (int i = 0; i < answer.size(); i++) {
        int mo_cnt = 0;
        int ja_cnt = 0;
        for (int j = 0; j < answer[i].size(); j++) {
            if (answer[i][j] == 'a' || answer[i][j] == 'e' || answer[i][j] == 'i' || answer[i][j] == 'o' || answer[i][j] == 'u') {
                mo_cnt++;
            }
            else {
                ja_cnt++;
            }
        }
        if (mo_cnt < 1 || ja_cnt < 2) {
            ind.push_back(i);
        }
    }

    for (int i = ind.size() - 1; i >= 0; i--) {
        answer.erase(answer.begin() + ind[i]);
    }

    for (int i = 0; i < answer.size(); i++) {
        cout << answer[i] << "\n";
    }

    return 0;
}

```
