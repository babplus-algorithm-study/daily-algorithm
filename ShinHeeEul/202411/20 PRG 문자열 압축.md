```java

class Solution
{

    public int solution(String s) {
        int answer = Integer.MAX_VALUE;

        int len = s.length();
        int count = 1;
        while(count <= len) {
            
            String tmp = "";
            int cnt = 1;
            String tt = "";
            
            for(int i = 0; i <= len - count; i+= count) {
                String t = s.substring(i, i + count);
                tt = s.substring(i + count, Math.min(i + 2 * count, len));
                if(!t.equals(tt)) {
                    if(cnt == 1) tmp += t;
                    
                    else {
                        tmp += cnt;
                        tmp += t;
                    }
                    
                    cnt = 1;
                } else {
                    cnt++;
                }
            }

            if(cnt == 1) {
                tmp += tt;
            }

            int a = tmp.length();
            if(cnt != 1) {
                a += count + 1;
            }
            
            count++;
            answer = Math.min(a, answer);
        }

        return answer;
    }
}

```
