```
#include <algorithm>
#include <cmath>
#include <iostream>
#include <vector>
#include <climits>
using namespace std;

struct Pos
{
    int x, y;
};
int N, M;
int MIN = INT_MAX;
bool selected[13];
vector<Pos> house_pos;
vector<Pos> chicken_pos;
vector<Pos> picked;

int Distance(Pos a, Pos b)
{
    return abs(a.x - b.x) + abs(a.y - b.y);
}

void Find_Min_Dist()
{
    int result = 0;
    for (int i = 0; i < house_pos.size(); i++)
    {
        int min_dist = INT_MAX;
        for (int j = 0; j < picked.size(); j++)
        {
            min_dist = min(min_dist, Distance(house_pos[i], picked[j]));
        }
        result += min_dist;
    }
    MIN = min(MIN, result);
}

void Find_M_Combination(int x, int m)
{
    if (m == M)
    { 
        Find_Min_Dist();
    }

    for (int i = x; i < chicken_pos.size(); i++)
    {
        if (selected[i] == true)
            continue;

        selected[i] = true;
        picked.push_back({ chicken_pos[i].x, chicken_pos[i].y });
        Find_M_Combination(i, m + 1);
        selected[i] = false;
        picked.pop_back();
    }
}

int main()
{
    cin >> N >> M;
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            int tmp;
            cin >> tmp;
            if (tmp == 1)
                house_pos.push_back({ i, j });
            else if (tmp == 2)
                chicken_pos.push_back({ i, j });
        }
    }
    Find_M_Combination(0, 0);
    cout << MIN << endl;
    return 0;
}
```
