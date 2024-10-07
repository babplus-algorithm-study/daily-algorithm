
```java
import java.util.*;
import java.io.*;

class Solution {
    PriorityQueue<Integer> pq = new PriorityQueue<>();
    
    public int[] solution(int[] fees, String[] records) {
        int MAX_MIN = 1439;
        
        HashMap<Integer, Integer> map = new HashMap<>();
        HashMap<Integer, Integer> sumMap = new HashMap<>();
        HashMap<Integer, Boolean> checkMap = new HashMap<>();
        

        
        for(int i = 0; i < records.length; i++) {
            String[] curInfo = records[i].split(" ");
            
            int curMin = getMin(curInfo[0]);
            int carNumber = Integer.parseInt(curInfo[1]);
            
            
            if(curInfo[2].equals("IN")) {
                int condition = map.getOrDefault(carNumber,-1);
                
                checkMap.put(carNumber,true);
                
                if(condition == -1) {
                    pq.add(carNumber);    
                }
                
                map.put(carNumber,curMin);            
            }
            
            else{
                checkMap.put(carNumber,false);
                int inTime = map.get(carNumber);
                int calTime = curMin - inTime;
                
                int value = sumMap.getOrDefault(carNumber,0);
                
                sumMap.put(carNumber,value + calTime);
            }
        }
        
        ArrayList<Integer> costs = new ArrayList<>();
        int[] answer = new int[pq.size()];
        while(!pq.isEmpty()) {
            int carNumber = pq.poll();
            
            int parkingTime = sumMap.getOrDefault(carNumber,-1);
    
            boolean flag = checkMap.get(carNumber);
            
                        if(parkingTime == -1) {
                int inMin = map.get(carNumber);
                int totalTime = calParkingTime(inMin, MAX_MIN);
                System.out.print(totalTime);
                costs.add(calCost(totalTime,fees));
                continue;
            }
            
            if(flag) {
                // 다시 들어와서 안나감
                parkingTime += calParkingTime(map.get(carNumber),MAX_MIN);
                costs.add(calCost(parkingTime,fees));
                continue;
            }
            

            
            costs.add(calCost(parkingTime,fees));   
        }
        
        for(int i = 0; i < costs.size(); i++) {
            answer[i] = costs.get(i);
        }
        
        return answer;
    }
    
    public static int calParkingTime(int inMin, int outMin) {
        return outMin - inMin;
    }
    
    public static int calCost(int parkingTime,int[] fees) {
        int originFee = fees[1];
        
        if(parkingTime <= fees[0]) {
            return originFee;
        }
        
        int time = parkingTime - fees[0];
        int c = time / fees[2];
        
        if(time % fees[2] == 0) {
            return originFee + (c * fees[3]) ;
        }    
        
        return originFee + ((c + 1) * fees[3]);
    }
    
    public static int getMin(String time) {
        String[] data = time.split(":");
        int hour = Integer.parseInt(data[0]);
        int min = Integer.parseInt(data[1]);
        
        int total  = 0;
        total += hour * 60;
        total += min; 
        
        return total;
    }
}
```