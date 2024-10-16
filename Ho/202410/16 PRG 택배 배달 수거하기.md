```java
import java.util.*;

class Solution {
    PriorityQueue<Box> pPq = new PriorityQueue<>();
    PriorityQueue<Box> dPq = new PriorityQueue<>();
    
        
    class Box implements Comparable<Box>{
        int cnt;
        int index;
        
        Box(int c, int i) {
            cnt = c;
            index = i;
        }
        @Override
        public int compareTo(Box o) {
            return o.index - this.index;
        }
    }
    
    // 배달하는게 제일 멀다
        //  수량도 많다.-> 배달하고 돌아오면서 수거하면 된다.
        // 
    
    // 근데 수거하는게 제일 먼 경우
        // 가는 길에 수거할 수 있도록 최대한 공간을 만들어 둔다.
        // 최대한 수거할 수 있음을 만족하면서
        // 배달도 많이 해야 함.
        
    
    
    public long solution(int cap, int n, int[] deliveries, int[] pickups) {
        long answer = 0;

        for(int i = 0; i < n; i++) {
            int dCnt = deliveries[i];
            int pCnt = pickups[i];
            
            if(dCnt > 0) {
                dPq.offer(new Box(dCnt, i));
            }
            
            if(pCnt > 0) {
                pPq.offer(new Box(pCnt, i));
            }
            
        }
        
        int poket = 0;
        
        while(!(dPq.isEmpty() && pPq.isEmpty())) {
            poket++;
            
            int curD = 0;
            int curP = 0;
            int maxDistance = 0;
            if(!dPq.isEmpty()){
                while(curD < cap && !dPq.isEmpty()) {
                    maxDistance = Math.max(maxDistance, dPq.peek().index);
                    if(dPq.peek().cnt > cap) {
                        Box temp = dPq.poll();
                        int remain = cap - curD;
                        
                        temp.cnt -= remain;
                        
                        dPq.add(temp);
                        curD = cap;
                    }
                    else{
                        Box temp = dPq.poll();
                        int remain = cap - curD;
                    
                        if(remain < temp.cnt) {
                            temp.cnt -= remain;
                            curD += remain;                            
                            dPq.add(temp);
                            continue;
                        }
                        curD += temp.cnt;
                    }
                }
            }
            curD = 0; 
            
            if(!pPq.isEmpty() ){
                while(curP < cap && !pPq.isEmpty()) {
                    maxDistance = Math.max(maxDistance, pPq.peek().index);
                    
                    if(pPq.peek().cnt > cap) {
                        Box temp = pPq.poll();
                        int remain = cap - curP;
                        temp.cnt -= remain;
                        pPq.add(temp);
                        curP = cap;
                    }
                    
                    else{
                        Box temp = pPq.poll();
                        int remain = cap - curP;
                    
                        if(remain < temp.cnt) {
                            temp.cnt -= remain;
                            curP += remain;
                            pPq.add(temp);
                            continue;
                        }
                        
                        curP += temp.cnt;
                    }
                }
            }
            curP = 0;
            
            answer += ((maxDistance+1) * 2);
        }
        
        return answer;
    }
}

```