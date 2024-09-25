
```java
// 할인율 : [10%, 20%, 30%, 40%]
class Solution {
    int[][] map;
    int[] discount = {10, 20, 30, 40};
    int[][] userss;
    int maxPeople = 0;
    int maxPrice = 0;
    
    public int[] solution(int[][] users, int[] emoticons) {
        map = new int[emoticons.length][4];
        userss = new int[users.length][2];
        for(int i = 0; i < users.length; i++) {
            int[] us = new int[2];
            us[1] = users[i][1];
            int per = users[i][0];
            if(per <= 10) us[0] = 0;
            else if(per <= 20) us[0] = 1;
            else if(per <= 30) us[0] = 2;
            else if(per <= 40) us[0] = 3;
            userss[i] = us.clone();
        }
        
        for(int i = 0; i < emoticons.length; i++) {
            for(int j = 0; j < 4; j++) {
                map[i][j] = emoticons[i] * (100 - discount[j]) / 100;
            }
            
        }
        
        backTracking(0, "");
        
        
        return new int[] {maxPeople, maxPrice};
    }
    
    public void backTracking(int count, String s) {
        if(count == map.length) {
            int people = 0;
            int price = 0;
            System.out.println("s" + s);
            for(int j = 0; j < userss.length; j++) {
                int[] user = userss[j];
                int tmp = 0;

                for(int i = 0; i < map.length; i++) {
                    int dc = Integer.parseInt((s.charAt(i) + ""));
                    if(dc >= user[0]) {
                        tmp += map[i][dc];
                    }
                }
                if(tmp >= user[1]) {
                    people++;
                } else {
                    price += tmp;
                }
            }
            if(people > maxPeople) {
                maxPeople = people;
                maxPrice = price;
            } else if(people == maxPeople && price > maxPrice) {
                maxPrice = price;
            }
            return;
        }
        
        for(int i = 0; i < 4; i++) {
            backTracking(count + 1, s + i);
        }
    }
    
}
```
