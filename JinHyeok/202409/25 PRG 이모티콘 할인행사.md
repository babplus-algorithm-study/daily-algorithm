```
#include <string>
#include <iostream>
#include <vector>
using namespace std;

int emo_size;
int sale[4] = {40,30,20,10};
vector<pair<int, int>> salePrice(7, {0, 0});
vector<int> result(2.0);

void dfs(vector<vector<int>> users, vector<int> emoticons, int cnt){
    
    if(cnt == emo_size){
        int total_price = 0;
        int people = 0;
        for(int i = 0; i < users.size(); i++){
            int price = 0;
            for(int j = 0; j < emo_size; j++){
                if(users[i][0] <= salePrice[j].second){
                    price += salePrice[j].first;
                }
            }
            
            if(price >= users[i][1]) {
                people++;
            } else {
                total_price += price;
            }
        }
        
        if(people > result[0]) {
            result[0] = people;
            result[1] = total_price;
        } else if(people == result[0] && total_price >= result[1]) {
            result[1] = total_price;
        }
        
        return;
    }
    
    for(int i = 0 ; i < 4; i++){
        salePrice[cnt].first = (100 - sale[i]) * emoticons[cnt] / 100;
        salePrice[cnt].second = sale[i];
        dfs(users, emoticons, cnt+1);
    }
}


vector<int> solution(vector<vector<int>> users, vector<int> emoticons) {
    emo_size = emoticons.size();
    dfs(users, emoticons, 0);
    
    
    return result;
}
```
