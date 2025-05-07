```
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>

using namespace std;

// 로마 숫자를 아라비아 숫자로 변환
int romanToInt(const string& s) {
    unordered_map<char, int> roman = {
        {'I', 1}, {'V', 5}, {'X', 10}, {'L', 50},
        {'C', 100}, {'D', 500}, {'M', 1000}
    };

    int total = 0;
    int prev = 0;

    for (int i = s.size() - 1; i >= 0; --i) {
        int curr = roman[s[i]];
        if (curr < prev)
            total -= curr;
        else {
            total += curr;
            prev = curr;
        }
    }

    return total;
}

string intToRoman(int num) {
    vector<pair<int, string>> value = {
        {1000, "M"}, {900, "CM"}, {500, "D"}, {400, "CD"},
        {100, "C"},  {90, "XC"},  {50, "L"},  {40, "XL"},
        {10, "X"},   {9, "IX"},   {5, "V"},   {4, "IV"},
        {1, "I"}
    };

    string result = "";
    for (const auto& [val, sym] : value) {
        while (num >= val) {
            result += sym;
            num -= val;
        }
    }

    return result;
}

int main() {
    string r1, r2;
    cin >> r1 >> r2;

    int num1 = romanToInt(r1);
    int num2 = romanToInt(r2);
    int sum = num1 + num2;

    cout << sum << endl;
    cout << intToRoman(sum) << endl;

    return 0;
}

```
