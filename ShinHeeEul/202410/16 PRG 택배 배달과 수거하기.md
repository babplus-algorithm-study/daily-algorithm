```java
import java.util.*;

class Solution {
    public long solution(int cap, int n, int[] deliveries, int[] pickups) {
        long answer = 0;
        
        PriorityQueue<Box> ppq = new PriorityQueue<>();
        ppq.add(new Box(0, 0));
        PriorityQueue<Box> dpq = new PriorityQueue<>();
        dpq.add(new Box(0, 0));
        
        int pcnt = 0;
        int dcnt = 0;
        for(int i = 0; i < n; i++) {
            pcnt += pickups[i];
            dcnt += deliveries[i];
            if(pickups[i] != 0)ppq.add(new Box(i + 1, pickups[i]));
            if(deliveries[i] != 0)dpq.add(new Box(i + 1, deliveries[i]));
        }
        
        int distance = 0;
        while(ppq.peek().value != 0 || dpq.peek().value != 0) {
            distance = Math.max(ppq.peek().index, dpq.peek().index);
            
            if(ppq.peek().value == 0) distance = dpq.peek().index;
            else if(dpq.peek().value == 0) distance = ppq.peek().index;
            
            if(distance == 0) break;
            int pmp = Math.min(cap, pcnt);
            int dmp = Math.min(cap, dcnt);
            
            while((pmp != 0 && ppq.peek().value != 0)){
                Box pic = ppq.poll();
                int picVal = pic.value;
                int min = Math.max(Math.min(pmp, picVal),0);
                pmp -= min;
                pic.value = picVal - min;
                pcnt -= min;
                ppq.add(pic);
            }
            
            while(dmp != 0 && dpq.peek().value != 0) {
                Box del = dpq.poll();
                int delVal = del.value;
                int min = Math.max(Math.min(dmp, delVal),0);
                dmp -= min;
                del.value -= min;
                dcnt -= min;
                dpq.add(del);
            }
            
            answer += (distance << 1);
        }
        return answer;
    }
    
    public class Box implements Comparable<Box> {
        int index;
        int value;
        
        public Box(int index, int value) {
            this.index = index;
            this.value = value;
        }
        
        public int compareTo(Box b) {
            if(this.value == 0 && b.value != 0) return 1;
            if(b.value == 0 && this.value != 0) return -1;
            return b.index - this.index;
        }
    }
}
```
