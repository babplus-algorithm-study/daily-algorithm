```
#include <string>
#include <vector>
using namespace std;
typedef long long ll;

ll solution(int cap, int n, vector<int> d, vector<int> p) {
    ll ans = 0;
    ll a = 0;
    ll b = 0;
    for(int i=n-1; i>=0; i--) {
        a -= d[i];
        b -= p[i];
        int cnt = 0;
        while(a < 0 || b < 0) {
            a += cap;
            b += cap;
            cnt++;
        }
        ans += (i + 1) * 2 * cnt;
    }
    return ans;
}
```
