```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;
 
public class Solution {
 
 
    static int[] arr;
    static int N;
    static int B;
    static int min = Integer.MAX_VALUE;
    public static void main(String[] args) throws IOException {
       BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
 
       int T = Integer.parseInt(br.readLine());
       StringBuilder sb = new StringBuilder();
       for(int t = 1; t <= T; t++) {
 
           min = Integer.MAX_VALUE;
           StringTokenizer st = new StringTokenizer(br.readLine());
           N = Integer.parseInt(st.nextToken());
           B = Integer.parseInt(st.nextToken());
 
           arr = new int[N];
           st = new StringTokenizer(br.readLine());
           for(int i = 0; i < N; i++) {
               arr[i] = Integer.parseInt(st.nextToken());
           }
           Arrays.sort(arr);
 
           backTracking(0,0, 0);
           sb.append("#").append(t).append(" ").append(min).append("\n");
       }
 
        System.out.println(sb);
    }
 
    public static void backTracking(int idx, int sum, int depth) {
        if(depth == N) return;
 
        for(int i = idx; i < N; i++) {
            int a = sum + arr[i];
            if(a >= B) {
                min = Math.min(min, a - B);
                return;
            }
            backTracking(i + 1, a, depth + 1);
        }
    }
}
```
