```java
package gold;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Collections;
import java.util.StringTokenizer;

public class P2212 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int k = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());

        int[] line = new int[n];

        for(int i = 0; i < n; i++) {
            line[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(line);

        Integer[] gap = new Integer[n-1];
        //각 격차를 구한다.
        for(int i =0; i < n-1; i++) {
            gap[i] = line[i+1] - line[i];
        }

        Arrays.sort(gap, Collections.reverseOrder());

        int ans = 0;

        for(int i = k-1; i < n-1; i++) {
            ans += gap[i];
        }

        System.out.println(ans);
    }
}

```