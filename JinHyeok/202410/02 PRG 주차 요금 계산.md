```
#include <iostream>
#include <string>
#include <vector>
#include <cmath>

using namespace std;
vector<pair<int, int>> car(10000, make_pair(-1, 0));


void seperate(string a){
    int hour = stoi(a.substr(0, 2));
    int minute = stoi(a.substr(3, 2));
    int carNumber = stoi(a.substr(6, 4));
    
    int timeNum = (hour * 60) + minute;
    
    if(a.substr(11,2) == "IN"){
        car[carNumber].first = timeNum;
    }
    else{
        car[carNumber].second = car[carNumber].second + timeNum - car[carNumber].first;
        car[carNumber].first = -1;
    }
}


vector<int> solution(vector<int> fees, vector<string> records) {
    vector<int> answer;
    
    for(int i = 0; i < records.size(); i++){
        seperate(records[i]);
    }
    
    for(int i = 0; i < car.size(); i++){
        if(car[i].first != -1){
            car[i].second = car[i].second + 1439 - car[i].first;
        }
    }
    
    
    for(int i = 0; i < car.size(); i++){
        if(car[i].second != 0){
            int price;
            if(ceil((double)(car[i].second - fees[0]) / fees[2]) * fees[3] < 0){
                price = fees[1];
            }
            else{
                price = fees[1] + ceil((double)(car[i].second - fees[0]) / fees[2]) * fees[3] ;
            }
            answer.push_back(price);            
        }
    }
    
    
    
    return answer;
}
```
