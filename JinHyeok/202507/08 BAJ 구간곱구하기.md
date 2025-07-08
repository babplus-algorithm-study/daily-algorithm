```
#include <iostream>
#include <vector>
using namespace std;
typedef unsigned long long ull;
vector<int> nums;
vector<ull> tree;
ull init(int start, int end, int node)
{
    if (start == end)
        return tree[node] = nums[start];
    int mid = (start + end) >> 1;
    int nextNode = node << 1;
    ull l = init(start, mid, nextNode);
    ull r = init(mid + 1, end, nextNode | 1);
    return tree[node] = (l * r) % 1000000007;
}
void update(int start, int end, int node, int target, int num)
{
    if (start > target || end < target)
        return;
    if (start == target && end == target)
    {
        tree[node] = num;
        return;
    }
    int mid = (start + end) >> 1;
    int nextNode = node << 1;
    if (start != end)
    {
        update(start, mid, nextNode, target, num);
        update(mid + 1, end, nextNode | 1, target, num);
    }
    tree[node] = (tree[nextNode] * tree[(nextNode | 1)]) % 1000000007;
}
ull find(int start, int end, int node, int left, int right)
{
    if (start > right || end < left)
        return 1;
    if (start >= left && end <= right)
    {
        return tree[node];
    }
    int mid = (start + end) >> 1;
    int nextNode = node << 1;
    ull l = find(start, mid, nextNode, left, right);
    ull r = find(mid + 1, end, nextNode | 1, left, right);
    return (l * r) % 1000000007;
}
int main()
{
    ios_base::sync_with_stdio(0), cin.tie(0);
    int N, M, K;
    cin >> N >> M >> K;
    nums = vector<int>(N + 1);
    tree = vector<ull>((N << 2), 1);
    for (int i = 1; i <= N; ++i)
    {
        cin >> nums[i];
    }
    init(1, N, 1);
    for (int i = 0; i < M + K; ++i)
    {
        int a, b, c;
        cin >> a >> b >> c;
        if (a == 1)
        {
            update(1, N, 1, b, c);
        }
        else
        {
            cout << find(1, N, 1, b, c) << "\n";
        }
    }
    return 0;
}
```
