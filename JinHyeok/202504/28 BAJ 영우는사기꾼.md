```
#include <iostream>
#include <vector>

using namespace std;

const int MAX = 100001;
int n, m, k;
vector<int> graph[MAX];
int indegree[MAX];
int buildCount[MAX];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    cin >> n >> m >> k;

    for (int i = 0; i < m; i++) {
        int x, y;
        cin >> x >> y;
        graph[x].push_back(y);
        indegree[y]++;
    }

    bool lier = false;
    for (int i = 0; i < k; i++) {
        int op, a;
        cin >> op >> a;
        
        if (op == 1) {
            if (indegree[a] > 0) {
                lier = true;
                break;
            }
            buildCount[a]++;
            if (buildCount[a] == 1) {
                for (int next : graph[a]) {
                    indegree[next]--;
                }
            }
        }
        else if (op == 2) {
            if (buildCount[a] == 0) {
                lier = true;
                break;
            }
            buildCount[a]--;
            if (buildCount[a] == 0) {
                for (int next : graph[a]) {
                    indegree[next]++;
                }
            }
        }
    }

    if (lier) cout << "Lier!\n";
    else cout << "King-God-Emperor\n";

    return 0;
}

```
