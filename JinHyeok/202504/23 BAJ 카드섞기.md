```
#include <bits/stdc++.h>

using namespace std;

int n;
vector<int> s, p, v1, v2;
set<vector<int>> visited;

void func(vector<int>& v1, vector<int>& v2)
{
	for (int i = 0; i < n; i++)
		v2[s[i]] = v1[i];
}

int check(vector<int>& v)
{
	int flag = 1;
	for (int i = 0; i < n; i++)
	{
		if (i % 3 != p[v[i]])
		{
			flag = 0;
			break;
		}
	}

	if (visited.find(v) == visited.end())
		visited.insert(v);
	else
		flag = 2;

	return flag;
}

int main(void)
{
	cin >> n;

	s.resize(n);
	p.resize(n);
	v1.resize(n);
	v2.resize(n);

	for (int i = 0; i < n; i++)
		cin >> p[i];

	for (int i = 0; i < n; i++)
		cin >> s[i];

	for (int i = 0; i < n; i++)
		v1[i] = i;

	int cnt = 0;
	bool flag = false;
	while (1)
	{
		int tmp = 0;
		if (!flag)
		{
			tmp = check(v1);			
			func(v1, v2);
		}
		else
		{
			tmp = check(v2);
			func(v2, v1);
		}

		if (tmp >= 1)
		{
			if (tmp == 2)
				cnt = -1;
			break;
		}

		flag = !flag;
		cnt++;
	}

	cout << cnt;
	return 0;
}
```
