```
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int n, k, a, st, r, start, end, mid, answer;
vector<int> v;

int main(void)
{
	cin >> n >> k;
    
	for (int i = 0; i < n; i++)
	{
		cin >> a;
		v.push_back(a);
	}
    
	sort(v.begin(), v.end());
	start = 1;                             
	end = v[n - 1] - v[0];

	while (start <= end)
	{
		r = 1;
		mid = (start + end) / 2;
		st = v[0];

		for (int i = 1; i < n; i++)
		{
			if (v[i] - st >= mid)
			{
				r++;
				st = v[i];
			}
		}

		if (r >= k)
		{
			answer = max(answer, mid);
			start = mid + 1;
		}

		else
			end = mid - 1;
	}
	cout << answer;
	return 0;
}
```
