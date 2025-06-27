```
#include <iostream>
#include <vector>
using namespace std;
typedef long long ll;

int N, M, K;
vector<ll> arr;
vector<ll> segTree;

ll init(int node, int start, int end) {
    if (start == end) return segTree[node] = arr[start];
    int mid = (start + end) / 2;
    return segTree[node] = init(node * 2, start, mid) + init(node * 2 + 1, mid + 1, end);
}

void update(int node, int start, int end, int idx, ll diff) {
    if (idx < start || idx > end) return;
    segTree[node] += diff;
    if (start != end) {
        int mid = (start + end) / 2;
        update(node * 2, start, mid, idx, diff);
        update(node * 2 + 1, mid + 1, end, idx, diff);
    }
}

ll query(int node, int start, int end, int left, int right) {
    if (right < start || end < left) return 0;
    if (left <= start && end <= right) return segTree[node];
    int mid = (start + end) / 2;
    return query(node * 2, start, mid, left, right) +
           query(node * 2 + 1, mid + 1, end, left, right);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    cin >> N >> M >> K;
    arr.resize(N + 1);
    segTree.resize(N * 4);

    for (int i = 1; i <= N; ++i) {
        cin >> arr[i];
    }

    init(1, 1, N);

    for (int i = 0; i < M + K; ++i) {
        int a;
        ll b, c;
        cin >> a >> b >> c;
        if (a == 1) {
            ll diff = c - arr[b];
            arr[b] = c;
            update(1, 1, N, b, diff);
        } else if (a == 2) {
            cout << query(1, 1, N, b, c) << "\n";
        }
    }

    return 0;
}

```
