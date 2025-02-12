```
#include <iostream>
#include <stack>

using namespace std;

int N, K;
stack<pair<int, int>> st;

int main() {
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    cin >> N;

    for(int i=1;i<=N;i++) {
        cin >> K;

        if(st.empty()) {
            st.push({i,K});
            cout << "0 ";
        }
        else {
            while(!st.empty()) {
                if(st.top().second > K) {
                    cout << st.top().first<< " ";
                    break;
                } else {
                    st.pop();
                }
            }
        if(st.empty()) cout << "0 ";

        st.push({i,K});
        }

    }
}
```
