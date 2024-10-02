```java
import java.util.*;

class Solution {
    public int[] solution(int[] fees, String[] records) {
        Map<String, Integer> map = new HashMap<>();
        Map<String, Integer> price = new HashMap<>();
        Map<String, Integer> queueTime = new HashMap<>();
        HashSet<String> set = new HashSet<>();
        
        PriorityQueue<String> pq = new PriorityQueue<>();
        Queue<Car> queue = new LinkedList<>();
        
        for(String rec : records) {
            StringTokenizer st = new StringTokenizer(rec);
            Car car = new Car(st.nextToken(), st.nextToken(), st.nextToken());
            set.add(car.number);
            queue.add(car);
        }
        
        while(!queue.isEmpty()) {
            Car car = queue.poll();
            
            //false일때?
            if(!car.isIn) {
                int time = map.getOrDefault(car.number, 0);
                StringTokenizer st1 = new StringTokenizer(car.time, ":");
                int outHour = Integer.parseInt(st1.nextToken());
                int outMin = Integer.parseInt(st1.nextToken());
                int allTime = outHour * 60 + outMin - time;
                
//                 if(allTime <= fees[0]) {
//                     price.put(car.number, price.getOrDefault(car.number, 0) + fees[1]);
//                 } else {
//                     int pr = fees[1] + (int) Math.ceil((double) (allTime - fees[0]) / (double) fees[2]) * fees[3];
//                     price.put(car.number, price.getOrDefault(car.number, 0) + pr);
//                 }
                
                queueTime.put(car.number, queueTime.getOrDefault(car.number, 0) + allTime);
                map.put(car.number, -1);
            }
            else {
                StringTokenizer st = new StringTokenizer(car.time, ":");
                int allTime = Integer.parseInt(st.nextToken()) * 60 + Integer.parseInt(st.nextToken());
                map.put(car.number, allTime);
            }
            
        }
        
        //map에 안비어있는 애들 끝까지 땡기고 끝
        int end = 23 * 60 + 59;
        for(String key : map.keySet()) {
            int time = map.getOrDefault(key, -1);
            int allTime = queueTime.getOrDefault(key, 0);
            if(time != -1) {
                int ti = end - time;
                allTime += ti;
            }
            
            if(allTime <= fees[0]) {
                    price.put(key, price.getOrDefault(key, 0) + fees[1]);
                } else {
                    int pr = fees[1] + (int) Math.ceil((double) (allTime - fees[0]) / (double) fees[2]) * fees[3];
                    price.put(key, price.getOrDefault(key, 0) + pr);
                }
        }
        
        int[] ans = new int[set.size()];
        
        for(String s : set) {
            pq.add(s);
        }
        
        for(int i = 0; i < ans.length; i++) {
            ans[i] = price.getOrDefault(pq.poll(), 0);
        }
        
        return ans;
    }
    
    public class Car implements Comparable<Car> {
        String time;
        String number;
        boolean isIn;
        
        public Car(String time, String number, String isIn) {
            this.time = time;
            this.number = number;
            this.isIn = isIn.equals("IN") ? true : false;
        }
        
        
        public int compareTo(Car c) {
            int b = c.number.compareTo(this.number);
            if(b < 0) {
                return -1;
            } else if(b > 0) {
                return 1;
            }
            return c.time.compareTo(this.time);
        }
        
        
    }
}
```
