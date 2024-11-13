```java
import java.util.*;

class Solution {
    public int solution(int[] queue1, int[] queue2) {
        int answer = 0;
        int max = queue1.length + queue2.length;
        
        long q1Sum = 0;
        long q2Sum = 0;
        Queue<Integer> q1 = new LinkedList<>();
        Queue<Integer> q2 = new LinkedList<>();
        
        for(int i = 0; i < queue1.length; i++) {
            q1Sum += queue1[i];
            q1.add(queue1[i]);
        }
        
        for(int i = 0; i < queue2.length; i++) {
            q2Sum += queue2[i];
            q2.add(queue2[i]);
        }
        
        while(true) {
            if(answer > (max << 1)) {
                return -1;
            }
            if(q1Sum == q2Sum) {
                return answer;
            }
            
            try {
                if(q1Sum > q2Sum) {
                    int tmp = q1.poll();
                    q2.add(tmp);
                    q1Sum -= tmp;
                    q2Sum += tmp;
                } else if(q1Sum < q2Sum) {
                    int tmp = q2.poll();
                    q1.add(tmp);
                    q2Sum -= tmp;
                    q1Sum += tmp;
                }
            } catch(Exception e) {
                return -1;
            }
            answer++;
        }
    }
    
    
}
```
