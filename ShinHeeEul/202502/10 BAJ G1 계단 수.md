```java
import java.util.*;

import java.io.*;

public class Main {

    static long[][][] dp;
    static int N;
    static final long MOD = 1000000000L;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
            if (N <= 9) {
                System.out.println(0);
                return;
            }

            // i는 현재 길이
            // j는 마지막 값
            // k는 현재 방문 값
            dp = new long[N + 1][10][(1 << 10)];

            for(int i = 1; i < 10; i++) {
                dp[1][i][(1 << i)] = 1;
            }

            for(int i = 2; i <= N; i++) {
                for(int j = 0; j < 10; j++) {
                    for(int k = 0; k < (1 << 10); k++) {
                        if(j == 0) dp[i][j][k | ( 1 << j)] += dp[i - 1][j + 1][k] %MOD;
                        else if(j == 9) dp[i][j][k | ( 1 << j)] += dp[i-1][j - 1][k] %MOD;
                        else dp[i][j][k | ( 1 << j)] += (dp[i-1][j-1][k] + dp[i-1][j+1][k]) %MOD;
                    }
                }
            }

            long sum = 0;

            for(int j = 0; j < 10; j++) {
                    sum += dp[N][j][(1<< 10) - 1] %MOD;
            }

            System.out.println(sum % MOD);

    }

}

```
