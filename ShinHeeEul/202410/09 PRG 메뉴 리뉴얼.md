```java
import java.util.*;

class Solution {
    ArrayList<String> answer;
    int[] visited = new int[26];
    int[] number = new int[26];
    int[] courseCount;
    ArrayList<String> max = new ArrayList<>();
    public ArrayList<String> solution(String[] orders, int[] course) {
        
        //사람들의 방문을 체크하는 방문 배열하나 두고(이진으로 구성)
        int all = 0;
        courseCount = new int[course.length];
        answer = new ArrayList<>();
        for(int i = 0; i < orders.length; i++) {
            all <<= 1;
            all++;
            String s = orders[i];
            for(int j = 0; j < s.length(); j++) {
                int a = 1;
                int idx = s.charAt(j) - 'A';
                a <<= i;
                visited[idx] += a;
                number[idx]++;
            }
        }
        
        for(int i = 0; i < course.length; i++) {
            max = new ArrayList<>();
            backTracking("", course[i], i, 0, all, 0);
            for(String s : max) {
                answer.add(s);
            }
        }
        
        Collections.sort(answer);
        
        return answer;
    }
    
    public void backTracking(String s, int n, int nIndex, int count, int v, int nxt) {
        if(count == n) {
            int cnt = 0;
            while(v != 0){
                cnt += (v & 1);
                v >>= 1;
            }
            if(cnt < 2) return;
            if(courseCount[nIndex] == cnt) {
                max.add(s);
            }
            if(courseCount[nIndex] < cnt) {
                max = new ArrayList<>();
                max.add(s);
                courseCount[nIndex] = cnt;
            }
            
            return;
        }
        
        for(int i = nxt; i < 26; i++) {
            if(number[i] < 2) continue;
            backTracking(s + (char) ('A' + i), n, nIndex, count + 1, v & visited[i], i + 1);
        }
        
    }
}
```
