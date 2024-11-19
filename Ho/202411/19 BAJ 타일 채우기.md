```java
package gold;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class P2133 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        int[] dp = new int[31];

        dp[0] = 1;
        dp[2] = 3;
        dp[4] = 11;

        if(n % 2 == 1) {
            System.out.println(0);
        }
        else{
            for(int i = 4; i <= n; i+=2 ) {
                dp[i] = dp[i - 2] * dp[2];
                for(int j = i-4; j >=0; j-=2 ) {
                    dp[i] = dp[i] + (dp[j] * 2);
                }
            }
            System.out.println(dp[n]);
        }
    }
}

```