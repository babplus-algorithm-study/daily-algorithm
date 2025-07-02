```
#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int N, M;
const int MAXN = 100000;
int arr[MAXN + 1];
vector<int> min_tree, max_tree;

void init(int node, int start, int end) {
    if (start == end) {
        min_tree[node] = max_tree[node] = arr[start];
        return;
    }
    int mid = (start + end) / 2;
    init(node * 2, start, mid);
    init(node * 2 + 1, mid + 1, end);
    min_tree[node] = min(min_tree[node * 2], min_tree[node * 2 + 1]);
    max_tree[node] = max(max_tree[node * 2], max_tree[node * 2 + 1]);
}

pair<int, int> findMinMax(int node, int start, int end, int left, int right) {
    if (right < start || end < left) {
        return make_pair(INT32_MAX, 0);
    }
    if (left <= start && end <= right) {
        return make_pair(min_tree[node], max_tree[node]);
    }
    int mid = (start + end) / 2;
    pair<int, int> l = findMinMax(node * 2, start, mid, left, right);
    pair<int, int> r = findMinMax(node * 2 + 1, mid + 1, end, left, right);
    return make_pair(min(l.first, r.first), max(l.second, r.second));
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> N >> M;
    int h = (int)ceil(log2(N));
    min_tree = vector<int>(1 << (h + 1));
    max_tree = vector<int>(1 << (h + 1));
    for (int i = 1; i <= N; ++i)
        cin >> arr[i];
    init(1, 1, N);
    int left, right;
    while (M--) {
        cin >> left >> right;
        pair<int, int> result = findMinMax(1, 1, N, left, right);
        cout << result.first << " " << result.second << "\n";
    }
    return 0;
}

```
